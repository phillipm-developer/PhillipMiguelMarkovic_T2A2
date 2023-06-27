from init import db, ma

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)
    role_desc = db.Column(db.Text())

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'role_name', 'role_desc')
