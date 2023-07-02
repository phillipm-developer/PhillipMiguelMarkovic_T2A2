from flask import Blueprint, request, abort
from datetime import timedelta
from models.user import User, UserSchema
from models.guardian_child import GuardianChild, GuardianChildSchema
from init import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

guardian_child_bp = Blueprint('guardians_children', __name__, url_prefix='/guardians_children')

# Returns all guardians_children on record - Includes their embedded User information
@guardian_child_bp.route('/', methods=['GET'])
@jwt_required()
def all_guardians_children():
    # select * from guardians_children;
    stmt = db.select(GuardianChild).order_by(GuardianChild.id.asc())
    guardians_children = db.session.scalars(stmt).all()
    return GuardianChildSchema(many=True, exclude=['child_id', 'guardian_id', 'relationship_id', 'guardian.user.role_id']).dump(guardians_children)

# Returns the guardian information for the guardian id supplied as a RESTful parameter
@guardian_child_bp.route('/<int:guardian_child_id>', methods=['GET'])
@jwt_required()
def one_guardian_child(guardian_child_id):
    stmt = db.select(GuardianChild).filter_by(id=guardian_child_id)
    guardian = db.session.scalar(stmt)

    if guardian:
        return GuardianChildSchema(exclude=['child_id', 'guardian_id', 'relationship_id', 'guardian.user.role_id']).dump(guardian)
    else:
        return {'error': 'Guardian-child relationship not found'}, 404

# Create - CRUD route for creating a new guardian in the database. 
@guardian_child_bp.route('/', methods=['POST'])
@jwt_required()
def create_guardian_child():
    try:
        # Parse, sanitize and validate the incoming JSON data 
        # via the GuardianChildschema
        guardian_child_info = GuardianChildSchema().load(request.json)
        print(guardian_child_info)

        guardian_child = GuardianChild(
            guardian_id = guardian_child_info['guardian_id'],
            child_id = guardian_child_info['child_id'],
            relationship_id = guardian_child_info['relationship_id']
        )

        # Add and commit the new guardian
        db.session.add(guardian_child)
        db.session.commit()

        return GuardianChildSchema(exclude=['child_id', 'guardian_id', 'relationship_id', 'guardian.user.role_id']).dump(guardian_child), 201
    
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409


# Update a guardian_child
@guardian_child_bp.route('/<int:guardian_child_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_guardian_child(guardian_child_id):
    stmt = db.select(GuardianChild).filter_by(id=guardian_child_id)
    guardian_child = db.session.scalar(stmt)
    guardian_child_info = GuardianChildSchema().load(request.json)

    print(guardian_child_info)

    if guardian_child:
        guardian_child.guardian_id = guardian_child_info.get('guardian_id', guardian_child.guardian_id)
        guardian_child.child_id = guardian_child_info.get('child_id', guardian_child.child_id)
        guardian_child.relationship_id = guardian_child_info.get('relationship_id', guardian_child.relationship_id)
        db.session.commit()
        return GuardianChildSchema(exclude=['child_id', 'guardian_id', 'relationship_id', 'guardian.user.role_id']).dump(guardian_child)
    else:
        return {'error': 'Guardian not found'}, 404

# Delete a guardian_child
@guardian_child_bp.route('/<int:guardian_child_id>', methods=['DELETE'])
@jwt_required()
def delete_guardian(guardian_child_id):
    stmt = db.select(GuardianChild).filter_by(id=guardian_child_id)
    guardian_child = db.session.scalar(stmt)

    if guardian_child:
        # admin_or_owner_required(guardian.user.id)
        db.session.delete(guardian_child)
        db.session.commit()
        return {"message": f"The records for guardian-child relationship #{guardian_child.id} have been deleted."}, 200
    else:
        return {'error': 'Guardian not found'}, 404

