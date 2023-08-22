from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email

#id, name, sallary, age, designation, yearsofwork

class CreateForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    sallary = FloatField("Sallary: ", validators=[DataRequired()])
    age = IntegerField("Age: ", validators=[DataRequired()])
    designation = StringField("Designation: ", validators=[DataRequired()])
    yearsofwork = IntegerField("Years in Company: ",validators=[DataRequired()])
    submit = SubmitField("Create")

class Updateform(FlaskForm):
    id = IntegerField("ID:", validators= [DataRequired()] )
    name = StringField("Name: ")
    sallary = FloatField("Sallary: ")
    age = IntegerField("Age: ")
    designation = StringField("Designation: ")
    yearsofwork = IntegerField("Years in Company: ")
    submit = SubmitField("Update")

class DeleteForm(FlaskForm):
    id = IntegerField("ID: ", validators=[DataRequired()])
    submit = SubmitField("Delete")
    
class GetOneForm(FlaskForm):
    id = IntegerField("ID: ", validators=[DataRequired()])
    submit = SubmitField("Get")
    

