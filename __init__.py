from extensions import db
from model import Patient
from server import create_app

app = create_app()

with app.app_context():
    db.create_all()
    print("Database initialized!")