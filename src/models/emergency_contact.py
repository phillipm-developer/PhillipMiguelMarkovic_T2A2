from init import db, ma

class EmergencyContact(db.Model):
    __tablename__ = 'emergency_contacts'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    relationship_id = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    notes = db.Column(db.Text())

class EmergencyContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'relationship_id', 'phone_number', 'notes')

