from flask import Flask, request, abort
from os import environ
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.guardian_bp import guardian_bp
from blueprints.child_bp import child_bp
from blueprints.guardian_child_bp import guardian_child_bp
from blueprints.user_bp import user_bp
from marshmallow.exceptions import ValidationError

def setup():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.__dict__['messages']}, 400


    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(guardian_bp)
    app.register_blueprint(child_bp)
    app.register_blueprint(guardian_child_bp)
    app.register_blueprint(user_bp)

    return app
