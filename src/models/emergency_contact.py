from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class EmergencyContact(db.Model):
    __tablename__ = 'emergency_contacts'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    relationship = db.Column(db.String())
    phone_number = db.Column(db.String())
    notes = db.Column(db.Text())

    child = db.relationship('Child', back_populates='emergency_contact')

class EmergencyContactSchema(ma.Schema):

    first_name = fields.String(required=False, validate=And(
        Length(min=2, max= 50, error='First name must be 2 to 50 characters long'),
        Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are permitted in a first name.')
    ))

    last_name = fields.String(required=False, validate=And(
        Length(min=2, max= 50, error='Last name must be 2 to 50 characters long'),
        Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are permitted in a last name.')
    ))

    relationship = fields.String(required=False)

    phone_number = fields.String(required=True, validate= Regexp('^[0-9 ()+]+$', error="Invalid phone number"))

    notes = fields.String(required=False)

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'relationship', 'phone_number', 'notes')
        ordered=True
