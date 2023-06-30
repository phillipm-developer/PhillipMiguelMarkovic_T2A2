from init import db, ma, VALID_GENDERS
from marshmallow import fields, validates_schema, validates
from marshmallow.exceptions import ValidationError
from marshmallow.validate import Length, OneOf, And, Regexp, Range
from datetime import date

class Child(db.Model):
    __tablename__ = 'children'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    date_of_birth = db.Column(db.Date())
    gender = db.Column(db.String)
    medical_info_id = db.Column(db.Integer)
    emergency_contact_id = db.Column(db.Integer)

    guardian_child = db.relationship('GuardianChild', back_populates='child')

class ChildSchema(ma.Schema):
    guardian_child = fields.List(fields.Nested('GuardianChildSchema'))

    first_name = fields.String(required=True, validate=And(
        Length(min=2, max= 50, error='First name must be 2 to 50 characters long'),
        Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are permitted in a first name.')
    ))

    last_name = fields.String(required=True, validate=And(
        Length(min=2, max= 50, error='Last name must be 2 to 50 characters long'),
        Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are permitted in a last name.')
    ))

    date_of_birth = fields.Date()

    gender = fields.String(load_default=VALID_GENDERS[0])

    @validates_schema()
    def validate_status(self, data, **kwargs):
        gender = [x for x in VALID_GENDERS if x.upper() == data['gender'].upper()]
        if len(gender) == 0:
            raise ValidationError(f'Gender can only be one of the following: {VALID_GENDERS}')

        data['gender'] = gender[0]

    
    @validates('date_of_birth') 
    def validate_enrollment_date(self, dob):
        today = date.today()

        # Determine the childs birthday this year
        this_year_birthday = date(today.year, dob.month, dob.day)

        if this_year_birthday < today:
            years = today.year - dob.year
        else:
            years = today.year - dob.year - 1

        # The child cannot be more than 6 years of age
        if years > 6:
            raise ValidationError("Child  must be 0-6 years of age.")

    class Meta:
        # fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'medical_info_id', 'emergency_contact_id', 'guardian_child')
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'medical_info_id', 'emergency_contact_id')
        ordered=True
