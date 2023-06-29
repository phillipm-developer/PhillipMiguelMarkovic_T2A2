from init import db, ma
from marshmallow import fields

class Guardian(db.Model):
    __tablename__ = 'guardians'

    id = db.Column(db.Integer, primary_key=True)

    occupation = db.Column(db.String(100), nullable=False)
    medical_info_consent = db.Column(db.Boolean, default=False)
    authorized_to_pickup = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='guardian')

    guardian_child = db.relationship('GuardianChild', back_populates='guardian')

class GuardianSchema(ma.Schema):
    # Tell marshmallow to use UserSchema to serialize 'user' field
    user = fields.Nested('UserSchema')
    guardian_child = fields.List(fields.Nested('GuardianChildSchema'))

    class Meta:
        fields = ('id', 'occupation', 'medical_info_consent', 'authorized_to_pickup', 'user', 'guardian_child')
