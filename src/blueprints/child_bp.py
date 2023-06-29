from flask import Blueprint, request, abort
from datetime import timedelta
from models.user import User, UserSchema
from models.child import Child, ChildSchema
from init import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

child_bp = Blueprint('children', __name__, url_prefix='/children')

# Returns all children on record - Includes their embedded User information
@child_bp.route('/', methods=['GET'])
def all_children():
    # select * from children;
    stmt = db.select(Child).order_by(Child.id.asc())
    children = db.session.scalars(stmt).all()
    return ChildSchema(many=True).dump(children)

# Returns the child information for the child id supplied as a RESTful parameter
@child_bp.route('/<int:child_id>', methods=['GET'])
def one_child(child_id):
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)

    if child:
        return ChildSchema(many=False).dump(child)
    else:
        return {'error': 'Child not found'}, 404

# Create - CRUD route for creating a new child in the database. 
@child_bp.route('/', methods=['POST'])
def create_child():
    try:
        # Parse, sanitize and validate the incoming JSON data 
        # via the schema
        child_info = ChildSchema().load(request.json)
        print(child_info)

        # Create a new Child model instance with the schema data
        child = Child(
            first_name = child_info['first_name'],
            last_name = child_info['last_name'],
            date_of_birth = child_info['date_of_birth'],
            gender = child_info['gender']
            # medical_info_id = child_info['medical_info_id'],
            # emergency_contact_id = child_info['emergency_contact_id']
        )

        # Add and commit the new child
        db.session.add(child)
        db.session.commit()

        # Return the new user excluding the password
        return ChildSchema().dump(child), 201
    
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409


# Update a card
@child_bp.route('/<int:child_id>', methods=['PUT', 'PATCH'])
def update_child(child_id):
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    child_info = ChildSchema().load(request.json)

    print(child_info)

    if child:
        # admin_or_owner_required(card.user.id)
        child.first_name = child_info.get('first_name', child.first_name)
        child.last_name = child_info.get('last_name', child.last_name)
        child.date_of_birth = child_info.get('date_of_birth', child.date_of_birth)
        child.gender = child_info.get('gender', child.gender)
        db.session.commit()
        return ChildSchema().dump(child)
    else:
        return {'error': 'Child not found'}, 404

# Delete a child
@child_bp.route('/<int:child_id>', methods=['DELETE'])
def delete_child(child_id):
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)

    if child:
        # admin_or_owner_required(child.user.id)
        db.session.delete(child)
        db.session.commit()
        return {"message": f"The records for child #{child.id} have been deleted."}, 200
    else:
        return {'error': 'Child not found'}, 404


def admin_required():
    user_email = get_jwt_identity()
    stmt = db.select(User).filter_by(email=user_email)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401)
