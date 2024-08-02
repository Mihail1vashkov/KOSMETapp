from flask import Flask, render_template, request, redirect, url_for
from models import db, Procedure, Appointment
import json
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///procedures.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/appointments')
def appointments():
    procedures = Procedure.query.all()
    return render_template('appointments.html', procedures=procedures)

@app.route('/book/<int:procedure_id>', methods=['GET'])
def book(procedure_id):
    procedure = Procedure.query.get_or_404(procedure_id)
    return render_template('book.html', procedure=procedure)

@app.route('/book/<int:procedure_id>', methods=['POST'])
def book_appointment(procedure_id):
    procedure = Procedure.query.get_or_404(procedure_id)
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')

    # Сохранение данных о записи в базу данных
    appointment = Appointment(
        procedure_id=procedure.id,
        name=name,
        email=email,
        phone=phone,
        appointment_time=datetime.now()  # Можно добавить конкретное время записи, если нужно
    )
    db.session.add(appointment)
    db.session.commit()

    return redirect(url_for('appointments'))

@app.route('/about')
def about():
    return render_template('about.html')

def create_tables():
    with app.app_context():
        db.create_all()
        with open('procedures.json', encoding='utf-8') as f:
            procedures_data = json.load(f)

        for procedure_data in procedures_data:
            appointment_time = datetime.strptime(procedure_data['appointment_time'], '%Y-%m-%d %H:%M:%S')
            procedure = Procedure(
                name=procedure_data['name'],
                description=procedure_data['description'],
                appointment_time=appointment_time
            )
            db.session.add(procedure)

        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
