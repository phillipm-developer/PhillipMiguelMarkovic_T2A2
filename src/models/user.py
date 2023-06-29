from init import db, ma
from marshmallow import fields

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

    guardian = db.relationship('Guardian', back_populates='user')

class UserSchema(ma.Schema):
    # guardian = fields.Nested('GuardianSchema', only=['occupation', 'medical_info_consent', 'authorized_to_pickup'])

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'date_of_birth', 'gender', 'role_id')
        ordered = True
