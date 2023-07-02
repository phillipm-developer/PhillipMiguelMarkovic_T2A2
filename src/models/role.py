from init import db, ma

# Model for the role table
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)
    role_desc = db.Column(db.Text())

    # Relationship formed with User model (one-to-many)
    user = db.relationship('User', back_populates='role')

class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'role_name', 'role_desc')
        ordered=True