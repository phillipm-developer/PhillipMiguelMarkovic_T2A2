from init import db, ma

class Child(db.Model):
    __tablename__ = 'children'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    date_of_birth = db.Column(db.Date())
    gender = db.Column(db.String)
    medical_info_id = db.Column(db.Integer)
    emergency_contact_id = db.Column(db.Integer)

class ChildSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'medical_info_id', 'emergency_contact_id')

