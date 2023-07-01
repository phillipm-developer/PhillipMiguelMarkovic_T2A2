from init import db, ma, VALID_GENDERS
from marshmallow import fields
from marshmallow.validate import Length, OneOf, And, Regexp, Range

class Guardian(db.Model):
    __tablename__ = 'guardians'

    id = db.Column(db.Integer, primary_key=True)

    occupation = db.Column(db.String(100), nullable=False)
    medical_info_consent = db.Column(db.Boolean, default=False)
    authorized_to_pickup = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='guardian')

    guardian_child = db.relationship('GuardianChild', back_populates='guardian', cascade='all, delete')

class GuardianSchema(ma.Schema):
    # Tell marshmallow to use UserSchema to serialize 'user' field
    user = fields.Nested('UserSchema')
    guardian_child = fields.List(fields.Nested('GuardianChildSchema'))

    occupation = fields.String(required=True, validate=And(
        Length(min=3, max= 100, error='Occupation must be 3 to 100 characters long'),
        Regexp('^[a-zA-Z ]+$', error='Only letters and spaces are permitted in an occupation.')
    ))

    medical_info_consent = fields.Boolean(default=False)
    authorized_to_pickup = fields.Boolean(default=False)

    class Meta:
        # fields = ('id', 'occupation', 'medical_info_consent', 'authorized_to_pickup', 'user', 'guardian_child')
        fields = ('id', 'occupation', 'medical_info_consent', 'authorized_to_pickup', 'user')
        ordered=True