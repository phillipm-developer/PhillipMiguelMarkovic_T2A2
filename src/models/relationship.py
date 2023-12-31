from init import db, ma

# Model for the relationships table - stores relationship types for use throughout the db.
class Relationship(db.Model):
    __tablename__ = 'relationships'

    id = db.Column(db.Integer, primary_key=True)
    relationship_name = db.Column(db.String(50), nullable=False)
    relationship_desc = db.Column(db.Text())

    # Relationship formed with the GuardianChild model
    guardian_child = db.relationship('GuardianChild', back_populates='relationship')

class RelationshipSchema(ma.Schema):
    class Meta:
        fields = ('id', 'relationship_name', 'relationship_desc')
        ordered=True