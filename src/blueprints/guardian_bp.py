from flask import Blueprint, request, abort
from datetime import timedelta
from models.user import User, UserSchema
from models.guardian import Guardian, GuardianSchema
from init import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

guardian_bp = Blueprint('guardians', __name__, url_prefix='/guardians')

# Returns all guardians on record - Includes their embedded User information
@guardian_bp.route('/', methods=['GET'])
def all_guardians():
    # select * from guardians;
    stmt = db.select(Guardian).order_by(Guardian.id.asc())
    guardians = db.session.scalars(stmt).all()
    return GuardianSchema(many=True, exclude=['user.password']).dump(guardians)

# Returns the guardian information for the guardian id supplied as a RESTful parameter
@guardian_bp.route('/<int:guardian_id>', methods=['GET'])
def one_guardian(guardian_id):
    stmt = db.select(Guardian).filter_by(id=guardian_id)
    guardian = db.session.scalar(stmt)

    if guardian:
        return GuardianSchema(exclude=['user.password']).dump(guardian)
    else:
        return {'error': 'Guardian not found'}, 404

# Create - CRUD route for creating a new guardian in the database. 
@guardian_bp.route('/', methods=['POST'])
def create_guardian():
    try:
        # Parse, sanitize and validate the incoming JSON data 
        # via the schema
        user_info = GuardianSchema().load(request.json)
        print(user_info)

        # Create a new User model instance with the schema data
        user = User(
            first_name = user_info['user']['first_name'],
            last_name = user_info['user']['last_name'],    
            email = user_info['user']['email'],
            password = bcrypt.generate_password_hash(user_info['user']['password']).decode('utf8'),
            phone_number = user_info['user']['phone_number'],
            date_of_birth = user_info['user']['date_of_birth'],
            gender = user_info['user']['gender'],
            role_id = user_info['user']['role_id']
        )

        # Add and commit the new user
        db.session.add(user)
        db.session.commit()

        print(user.id)

        guardian = Guardian(
            user_id = user.id,
            occupation = user_info['occupation'],
            medical_info_consent = user_info['medical_info_consent'],
            authorized_to_pickup = user_info['authorized_to_pickup']
        )

        # Add and commit the new guardian
        db.session.add(guardian)
        db.session.commit()

        # Return the new user excluding the password
        return GuardianSchema(exclude=['user.password']).dump(guardian), 201
    
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409


# Update a card
@guardian_bp.route('/<int:guardian_id>', methods=['PUT', 'PATCH'])
def update_guardian(guardian_id):
    stmt = db.select(Guardian).filter_by(id=guardian_id)
    guardian = db.session.scalar(stmt)
    guardian_info = GuardianSchema().load(request.json)

    print(guardian_info)

    if guardian:
        # admin_or_owner_required(card.user.id)
        guardian.occupation = guardian_info.get('occupation', guardian.occupation)
        guardian.medical_info_consent = guardian_info.get('medical_info_consent', guardian.medical_info_consent)
        guardian.authorized_to_pickup = guardian_info.get('authorized_to_pickup', guardian.authorized_to_pickup)
        db.session.commit()
        return GuardianSchema(exclude=['user.password']).dump(guardian)
    else:
        return {'error': 'Guardian not found'}, 404

# Delete a guardian
@guardian_bp.route('/<int:guardian_id>', methods=['DELETE'])
def delete_guardian(guardian_id):
    stmt = db.select(Guardian).filter_by(id=guardian_id)
    guardian = db.session.scalar(stmt)

    if guardian:
        # admin_or_owner_required(guardian.user.id)
        db.session.delete(guardian)
        db.session.commit()
        return {"message": f"The records for guardian #{guardian.id} have been deleted."}, 200
    else:
        return {'error': 'Guardian not found'}, 404


def admin_required():
    user_email = get_jwt_identity()
    stmt = db.select(User).filter_by(email=user_email)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401)
