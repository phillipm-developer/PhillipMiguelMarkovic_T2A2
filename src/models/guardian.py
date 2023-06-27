from init import db, ma

class Guardian(db.Model):
    __tablename__ = 'guardians'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    medical_info_consent = db.Column(db.Boolean, default=False)
    authorized_to_pickup = db.Column(db.Boolean, default=False)

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'occupation', 'medical_info_consent', 'authorized_to_pickup')
