from init import db, ma

class AuthorizedPickup(db.Model):
    __tablename__ = 'authorized_pickups'

    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('children.id'))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    relationship_id = db.Column(db.Integer, db.ForeignKey('relationships.id'))
    phone_number = db.Column(db.String)

class AuthorizedPickupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'relationship_id', 'phone_number')

 