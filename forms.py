#WTForms is a flexible forms validation and rendering library for python web development.
from flask import Flask,render_template
 #Flask-WTF to handle and validate form data 
from flask_wtf import FlaskForm
# imported a few useful classes from Flask-WTF — the base StringField a text field, a textarea field 
from wtforms import StringField,TextField,validators,Field,PasswordField,BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired,Length,DataRequired,ValidationError
app= Flask(__name__)
#LoginForm is a class inherit from FlaskForm
class ContactForm(FlaskForm):
    fname = StringField('Firstname', [InputRequired()])
    def validate_fname(self, field):
        value1=field.data
        if len(value1) > 10 or len(value1) <5:
            raise ValidationError('Name length range between 5 to 10 characters  only')
        elif value1.isdigit()==True:
            raise ValidationError('Name should be  characters  only')
    lname = StringField('Lastname', [InputRequired()])
    def validate_lname(self, field):
        value2=field.data
        if len(value2) > 10 or len(value2) <5:
            raise ValidationError('Name length range between 5 to 10 characters  only')
        elif value2.isdigit()==True:
            raise ValidationError('Name should be  characters  only')
    age=TextField('Age',[InputRequired()])
    def validate_age(self,field):
        value3=field.data
        if int(value3) <18:
            raise ValidationError('Age should be between 18 and 100 yrs only')
    email=EmailField('email', [validators.DataRequired(), validators.Email(message="Email is required")])
    mobileno=TextField('Mobileno',[InputRequired()])
    def validate_mobileno(self,field):
        value4=field.data
        if len(value4) <10:
            raise ValidationError('mobileno should be length 10 numbers')
        elif value4.isdigit==False:
            raise ValidationError('mobileno should be only numbers')
    password=PasswordField('Password',[InputRequired()])
    def validate_password(self, field):
        value2=field.data
        if len(value2) > 10 or len(value2) <5  :
            raise ValidationError('password should be  between 5 to 10 characters  only')    
class LoginForm(FlaskForm):
    Firstname = StringField('Firstname', [InputRequired()])
    def validate_Firstname(self, field):
        value1=field.data
        if len(value1) > 10 or len(value1) <5  :
            raise ValidationError('Name length range between 5 to 10 characters  only')
    password=PasswordField('Password',[InputRequired()])
    def validate_password(self, field):
        value2=field.data
        if len(value2) > 10 or len(value2) <5  :
            raise ValidationError('password should be  between 5 to 10 characters  only')
class UpdateForm(FlaskForm):
    fname = StringField('Firstname', [InputRequired()])
    def validate_fname(self, field):
        value1=field.data
        if len(value1) > 10 or len(value1) <5  :
            raise ValidationError('Name length range between 5 to 10 characters  only')
        elif value1.isdigit()==True:
            raise ValidationError('Name should be  characters  only')
    lname = StringField('Lastname', [InputRequired()])
    def validate_lname(self, field):
        value2=field.data
        if len(value2) > 10 or len(value2) <5:
            raise ValidationError('Name length range between 5 to 10 characters  only')
        elif value2.isdigit()==True:
            raise ValidationError('Name should be  characters  only')
    age=TextField('Age',[InputRequired()])
    def validate_age(self,field):
        value3=field.data
        if int(value3) <18:
            raise ValidationError('Age should be between 18 and 100 yrs only')
    email=EmailField('email', [validators.DataRequired(), validators.Email(message="Email is required")])
    mobileno=TextField('Mobileno',[InputRequired()])
    def validate_mobileno(self,field):
        value4=field.data
        if len(value4) <10:
            raise ValidationError('mobileno should be length 10 numbers')
        elif value4.isdigit==False:
            raise ValidationError('mobileno should be only numbers')
    password=PasswordField('Password',[InputRequired()])
    def validate_password(self, field):
        value2=field.data
        if len(value2) > 10 or len(value2) <5  :
            raise ValidationError('password should be  between 5 to 10 characters  only')   
