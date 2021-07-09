from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from jobfinder.models import User

#Registraion form 
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists! Please try different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists! Please try different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ProfileForm(FlaskForm):

    basic_choice = ['Yes', 'No']
    auth_choices = ['US Citizen', 'EAD', 'OPT EAD', 'Green Card', 'H1-B work visa']
    jtype_choices = ['Fulltime', 'Part-time', 'Contract', 'Internship']
    full_name = StringField('Legal Name:', validators=[DataRequired()]) 
    position_int = StringField('Position intersted in:', validators=[DataRequired()])
    job_type = SelectField('Job type:', choices=jtype_choices, validators=[DataRequired()])
    city = StringField('City:', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    #upload resume
    
    skills = StringField('Add your skills:', validators=[DataRequired()])
    work_status = SelectField('Are you eligible to work here in the United States ? Yes or No:', 
                    choices=basic_choice, validators=[DataRequired()]) 
    work_auth = SelectField('Work Authorization?', choices=auth_choices, validators=[DataRequired()])
    remote = SelectField('Remote ? Yes or No:',choices=basic_choice, validators=[DataRequired()])
    submit = SubmitField('Save')