from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import input_required, number_range

class Prediction(FlaskForm):
    PatientCT= IntegerField('Clump Thickness', validators=[input_required(), number_range(min=0, max=10, message="Chose a Number Between 0 and 10")])
    PatientUCSize= IntegerField('Uniformity Of Cell Size', validators=[input_required(), number_range(min=0, max=10, message="Chose a Number Between 0 and 10")])
    PatientUCShape= IntegerField('Uniformity Of Cell Shape', validators=[input_required(), number_range(min=0, max=10, message="Chose a Number Between 0 and 10")])
    PatientMA= IntegerField('Uniformity Of Marginal Adhesion', validators=[input_required(), number_range(min=0, max=10, message="Chose a Number Between 0 and 10")])
    PatientSECS= IntegerField('Uniformity Of Single Epithelial Cell Size', validators=[input_required(), number_range(min=0, max=10, message="Chose a Number Between 0 and 10")])
    PatientBN= IntegerField('Bare Nuclei', validators=[input_required(), number_range(min=0, max=10, message="Chose a Number Between 0 and 10")])
    PatientBC= IntegerField('Bland Chromatin', validators=[input_required(), number_range(min=0, max=10, message="Chose a Number Between 0 and 10")])
    PatientNN= IntegerField('Normal Nucleoli', validators=[input_required(), number_range(min=0, max=10, message="Chose a Number Between 0 and 10")])
    PatientMitosis= IntegerField('Mitosis', validators=[input_required(), number_range(min=0, max=10, message="Chose a Number Between 0 and 10")])
    Submit= SubmitField(' Predict ')