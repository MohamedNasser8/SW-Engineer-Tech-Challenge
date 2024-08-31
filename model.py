from extensions import db


class Patient(db.Model):
    __tablename__ = 'patients'

    SeriesInstanceUID = db.Column(db.String(255), primary_key=True)
    PatientName = db.Column(db.String(255), nullable=False)
    PatientID = db.Column(db.String(255), nullable=False)
    StudyInstanceUID = db.Column(db.String(255), nullable=False)
    InstancesInSeries = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Patient {self.PatientName}>'
