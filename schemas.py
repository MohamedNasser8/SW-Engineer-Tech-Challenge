from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from model import Patient

class PatientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Patient
        load_instance = True
