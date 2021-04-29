from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # Add the following fields to the form class:
    # - title - StringField
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=50)])
    # - address - StringField
    address = StringField('Address', validators=[DataRequired(), Length(min=5, max=70)])
    # - submit button
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # Add the following fields to the form class:
    # - name - StringField
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=70)])
    # - price - FloatField
    name = FloatField('Price', validators=[DataRequired()])
    # - category - SelectField (specify the 'choices' param)
    category = SelectField('Category', choices=['Produce', 'Deli', 'Bakery', 'Pantry', 'Frozen', 'Other'], validators=[DataRequired()])
    # - photo_url - StringField (use a URL validator)
    photo_url = StringField('Photo Link', validators=[DataRequired()])
    # - store - QuerySelectField (specify the `query_factory` param)
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, allow_blank=False, get_label='title')
    # - submit button
    submit = SubmitField('Submit')

# forms.py

class SignUpForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

