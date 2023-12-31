from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

# Put this here so other models can access it - DRY
VALID_GENDERS = ['Male', 'Female', 'Non-binary']
