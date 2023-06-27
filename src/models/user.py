from init import db, ma

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date())
    gender = db.Column(db.String)
    role_id = db.Column(db.Integer, nullable=False)

    # is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'password', 'phone_number', 'date_of_birth', 'gender', 'role_id')

