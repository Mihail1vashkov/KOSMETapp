from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    name = StringField('Procedure Name', validators=[DataRequired()])
    appointment_time = DateTimeField('Appointment Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Schedule Appointment')
