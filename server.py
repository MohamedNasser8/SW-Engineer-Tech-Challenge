import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv


from extensions import db
from model import Patient
from schemas import PatientSchema


def create_app():
    load_dotenv()

    app = Flask(__name__)

    # Load environment variables to configure the app and database
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() in ['true', 'on', '1']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO', 'False').lower() in ['true', 'on', '1']

    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})


    db.init_app(app)

    @app.route('/save_series', methods=['POST'])
    def save_series():
        try:
            series_data = request.json
            patient_schema = PatientSchema()
            patient = patient_schema.load(series_data, session=db.session)
            db.session.add(patient)
            db.session.commit()
            return jsonify({'message': "Data saved successfully"}), 200
        except Exception as e:
            return jsonify({'message': f"An error occurred: {str(e)}"}), 500

    @app.route('/', methods=['GET'])
    def get_patients():
        try:
            patient_schema = PatientSchema(many=True)

            patients = db.session.query(Patient).all()

            return jsonify(patient_schema.dump(patients)), 200
        except Exception as e:
            return jsonify({'message': f"An error occurred: {str(e)}"}), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
