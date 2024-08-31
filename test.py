import json

import pytest
from extensions import db
from server import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


def test_save_series(client):
    patient_data = {
        "SeriesInstanceUID": "123456",
        "PatientID": "123",
        "PatientName": "John Doe",
        "StudyInstanceUID": "123456",
        "InstancesInSeries": 1
    }
    response = client.post('/save_series',
                                json=patient_data,
                                content_type='application/json')
    assert response.status_code == 200
    assert response.json == {'message': "Data saved successfully"}

    # Verify data in the database
    from model import Patient
    patient = Patient.query.first()

    assert patient.SeriesInstanceUID == "123456"