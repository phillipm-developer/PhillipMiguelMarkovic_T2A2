from flask import Blueprint, request, abort
from datetime import timedelta
from models.user import User, UserSchema
from models.user import User, UserSchema
from init import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

user_bp = Blueprint('users', __name__, url_prefix='/users')

# Returns all users on record - Includes their embedded role information
@user_bp.route('/', methods=['GET'])
@jwt_required()
def all_users():
    # select * from users;
    stmt = db.select(User).order_by(User.id.asc())
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True, exclude=['password', 'role_id']).dump(users)

# Returns the user information for the user id supplied as a RESTful parameter
@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def one_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)

    if user:
        return UserSchema(many=False, exclude=['password', 'role_id']).dump(user)
    else:
        return {'error': f'User #{user_id} not found'}, 404

# Create - CRUD route for creating a new user in the database. 
@user_bp.route('/', methods=['POST'])
@jwt_required()
def create_user():
    try:
        # Parse, sanitize and validate the incoming JSON data 
        # via the schema
        user_info = UserSchema().load(request.json)
        print(user_info)

        # Create a new User model instance with the schema data
        user = User(
            first_name = user_info['first_name'],
            last_name = user_info['last_name'],
            email = user_info['email'],
            password = user_info['password'],
            phone_number = user_info['phone_number'],
            date_of_birth = user_info['date_of_birth'],
            gender = user_info['gender'],
            role_id = user_info['role_id']
        )

        # Add and commit the new user
        db.session.add(user)
        db.session.commit()

        # Return the new user excluding the password
        return UserSchema(exclude=['role_id']).dump(user), 201
    
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409


# Update a user
@user_bp.route('/<int:user_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    user_info = UserSchema().load(request.json)

    print(user_info)

    if user:
        user.first_name = user_info.get('first_name', user.first_name)
        user.last_name = user_info.get('last_name', user.last_name)
        user.email = user_info.get('email', user.email)
        user.password = user_info.get('password', user.password)
        user.date_of_birth = user_info.get('date_of_birth', user.date_of_birth)
        user.gender = user_info.get('gender', user.gender)
        user.phone_number = user_info.get('phone_number', user.phone_number)
        user.role_id = user_info.get('role_id', user.role_id)

        db.session.commit()
        return UserSchema().dump(user)
    else:
        return {'error': f'User #{user_id} not found'}, 404

# Delete a user
@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)

    if user:
        # admin_or_owner_required(user.user.id)
        db.session.delete(user)
        db.session.commit()
        return {"message": f"The records for user #{user.id} - {user.first_name} {user.last_name} have been deleted."}, 200
    else:
        return {'error': f'User #{user_id} not found'}, 404


