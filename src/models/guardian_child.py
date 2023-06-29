from init import db, ma
from marshmallow import fields

class GuardianChild(db.Model):
    __tablename__ = 'guardians_children'

    id = db.Column(db.Integer, primary_key=True)

    guardian_id = db.Column(db.Integer, db.ForeignKey('guardians.id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('children.id'), nullable=False)

    relationship_id = db.Column(db.Integer, db.ForeignKey('relationships.id'))

    # guardian = db.relationship('Guardian', back_populates='guardians_children')
    # child = db.relationship('Child', back_populates='guardians_children')


class GuardianChildSchema(ma.Schema):
    # guardian = fields.Nested('GuardianSchema', only=['occupation'])
    # child = fields.Nested('ChildSchema', only=['first_name'])

    class Meta:
        fields = ('id', 'guardian', 'child_id', 'child')
