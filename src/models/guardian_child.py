from init import db, ma

class GuardianChild(db.Model):
    __tablename__ = 'guardians_children'

    id = db.Column(db.Integer, primary_key=True)
    guardian_id = db.Column(db.Integer, nullable=False)
    child_id = db.Column(db.Integer, nullable=False)
    relationship_id = db.Column(db.Integer, nullable=False)

class GuardianChildSchema(ma.Schema):
    class Meta:
        fields = ('id', 'guardian_id', 'child_id', 'relationship_id')
