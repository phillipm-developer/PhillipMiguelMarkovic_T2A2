from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class MedicalInformation(db.Model):
    __tablename__ = 'medical_information'

    id = db.Column(db.Integer, primary_key=True)
    dietary_restrictions = db.Column(db.Text())
    allergies = db.Column(db.Text())
    medications = db.Column(db.Text())
    special_needs = db.Column(db.Text())
    notes = db.Column(db.Text())

    child = db.relationship('Child', back_populates='medical_info')

class MedicalInformationSchema(ma.Schema):

    dietary_restrictions = fields.String(required=False)

    allergies = fields.String(required=False)

    medications = fields.String(required=False)

    special_needs = fields.String(required=False)

    notes = fields.String(required=False)

    class Meta:
        fields = ('id', 'dietary_restrictions', 'allergies', 'medications', 'special_needs', 'notes')
        ordered=True
