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
    

