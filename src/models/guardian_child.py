from init import db, ma
from marshmallow import fields

# ORM model for join table guardians_children
class GuardianChild(db.Model):
    __tablename__ = 'guardians_children'

    id = db.Column(db.Integer, primary_key=True)

    guardian_id = db.Column(db.Integer, db.ForeignKey('guardians.id'), nullable=False)

    # Relationship formed with Guardian model
    guardian = db.relationship('Guardian', back_populates='guardian_child')

    child_id = db.Column(db.Integer, db.ForeignKey('children.id'), nullable=False)

    # Relationship formed with Child model
    child = db.relationship('Child', back_populates='guardian_child')

    relationship_id = db.Column(db.Integer, db.ForeignKey('relationships.id'))

    # Relationship formed with Relationship model
    relationship = db.relationship('Relationship', back_populates='guardian_child')


class GuardianChildSchema(ma.Schema):
    guardian = fields.Nested('GuardianSchema', exclude=['user.password'])
    child = fields.Nested('ChildSchema', only=['id', 'first_name', 'last_name', 'date_of_birth', 'gender'])
    relationship = fields.Nested('RelationshipSchema')

    # Validations
    guardian_id = fields.Integer(required=True)
    child_id = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'guardian_id', 'guardian', 'child_id', 'child', 'relationship_id', 'relationship')
        ordered=True