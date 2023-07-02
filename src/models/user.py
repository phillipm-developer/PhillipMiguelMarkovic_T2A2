from init import db, ma, VALID_GENDERS
from marshmallow import fields, validates_schema
from marshmallow.exceptions import ValidationError
from marshmallow.validate import Length, OneOf, And, Regexp, Range, Email

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date())
    gender = db.Column(db.String)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', back_populates='user')

    guardian = db.relationship('Guardian', back_populates='user', cascade='all, delete')

class UserSchema(ma.Schema):
    role = fields.Nested('RoleSchema')

    first_name = fields.String(required=True, validate=And(
        Length(min=2, max= 50, error='First name must be 2 to 50 characters long'),
        Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are permitted in a first name.')
    ))

    last_name = fields.String(required=True, validate=And(
        Length(min=2, max= 50, error='Last name must be 2 to 50 characters long'),
        Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are permitted in a last name.')
    ))

    # Use the email validator provided by marshmallow.validate
    email = fields.String(required=True, validate=Email(error="Please provide a valid email address"))

    password = fields.String(required=True, validate=Length(min=10, max=100, error="Your password must be at least 10 characters long"))

    phone_number = fields.String(required=True, validate= Regexp('^[0-9 ()+]+$', error="Invalid phone number"))

    date_of_birth = fields.Date()

    @validates_schema()
    def validate_status(self, data, **kwargs):
        gender = [x for x in VALID_GENDERS if x.upper() == data['gender'].upper()]
        if len(gender) == 0:
            raise ValidationError(f'Gender can only be one of the following: {VALID_GENDERS}')

        data['gender'] = gender[0]

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'date_of_birth', 'gender', 'role_id', 'role')
        ordered = True
