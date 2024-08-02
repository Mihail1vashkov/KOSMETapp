from app import app, db
import json
from datetime import datetime
from models import Procedure

def init_db():
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
        print("Database initialized and data added.")

if __name__ == '__main__':
    init_db()
