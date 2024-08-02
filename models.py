from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Procedure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    appointment_time = db.Column(db.DateTime, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    procedure_id = db.Column(db.Integer, db.ForeignKey('procedure.id'), nullable=False)
    procedure = db.relationship('Procedure', backref=db.backref('appointments', lazy=True))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
