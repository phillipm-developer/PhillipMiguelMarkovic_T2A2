from flask import Blueprint, request, abort
from datetime import timedelta
from models.user import User, UserSchema
from models.child import Child, ChildSchema
from init import db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required
from models.medical_information import MedicalInformation, MedicalInformationSchema
from models.emergency_contact import EmergencyContact, EmergencyContactSchema

child_bp = Blueprint('children', __name__, url_prefix='/children')

# Returns all children on record - Includes their embedded User information
@child_bp.route('/', methods=['GET'])
@jwt_required()
def all_children():
    # select * from children;
    stmt = db.select(Child).order_by(Child.id.asc())
    children = db.session.scalars(stmt).all()
    return ChildSchema(many=True, exclude=['medical_info', 'emergency_contact']).dump(children)

# Returns the child information for the child id supplied as a RESTful parameter
@child_bp.route('/<int:child_id>', methods=['GET'])
@jwt_required()
def one_child(child_id):
    # select * from children where id=child_id
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)

    if child:
        return ChildSchema(many=False, exclude=['medical_info', 'emergency_contact']).dump(child)
    else:
        return {'error': 'Child not found'}, 404

# Returns the medical information record for child_id
@child_bp.route('/<int:child_id>/medical_info', methods=['GET'])
@jwt_required()
def one_child_with_medical_info(child_id):
    # select * from children, medical_information where id=child_id and 
    # children.medical_information_id=medical_information.id
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)

    if child:
        return ChildSchema(many=False, exclude=['medical_info_id', 'emergency_contact']).dump(child)
    else:
        return {'error': 'Child not found'}, 404

# Returns the medical information record for child_id
@child_bp.route('/<int:child_id>/emergency_contact', methods=['GET'])
@jwt_required()
def one_child_with_emergency_contact(child_id):
    # select * from children, emergency_contacts where id=child_id and 
    # children.emergency_contact_id=emergency_contacts.id
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)

    if child:
        return ChildSchema(many=False, exclude=['medical_info', 'emergency_contact_id']).dump(child)
    else:
        return {'error': 'Child not found'}, 404


# Create - CRUD route for creating a new child in the database. 
@child_bp.route('/', methods=['POST'])
@jwt_required()
def create_child():
    try:
        # Parse, sanitize and validate the incoming JSON data 
        # via the schema
        child_info = ChildSchema().load(request.json)

        # For every child that is created a corresponding default medical inforation entry is made with 
        # no inforamtion recorded. - insert into medical_information (dietary_restrictions, ...) values (..., ...)
        medical_info = MedicalInformation(
            dietary_restrictions ="",
            allergies ="",
            medications ="",
            special_needs ="",
            notes =""
        )

        # Add and commit the new medical info entity
        db.session.add(medical_info)
        db.session.commit()

        # For every child thats created a corresponding default emergency contact is created. This subsequestly updated 
        # by an admin or guardian. - insert into emergency_contacts (first_name, ...) values (..., ...)
        emergency_contact = EmergencyContact(
            first_name = "",
            last_name = "",
            relationship = "",
            phone_number = "",
            notes = ""
        )

        # Add and commit the new emergency contact entity
        db.session.add(emergency_contact)
        db.session.commit()

        # Create a new Child model instance with the schema data
        child = Child(
            first_name = child_info['first_name'],
            last_name = child_info['last_name'],
            date_of_birth = child_info['date_of_birth'],
            gender = child_info['gender'],
            medical_info_id = medical_info.id,
            emergency_contact_id = emergency_contact.id
        )

        # Add and commit the new child
        db.session.add(child)
        db.session.commit()

        # Return the new user excluding the password
        return ChildSchema(exclude=['medical_info', 'emergency_contact']).dump(child), 201
    
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409

# Update a child
@child_bp.route('/<int:child_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_child(child_id):
    # update child set first_name="...", last_name="..." where id=child_id
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    child_info = ChildSchema().load(request.json)

    if child:
        child.first_name = child_info.get('first_name', child.first_name)
        child.last_name = child_info.get('last_name', child.last_name)
        child.date_of_birth = child_info.get('date_of_birth', child.date_of_birth)
        child.gender = child_info.get('gender', child.gender)
        db.session.commit()
        return ChildSchema().dump(child)
    else:
        return {'error': 'Child not found'}, 404

@child_bp.route('/<int:child_id>/medical_info', methods=['PUT', 'PATCH'])
@jwt_required()
def update_child_medical_record(child_id):
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    medical_info = MedicalInformationSchema().load(request.json)

    if child:
        child.medical_info.dietary_restrictions = medical_info.get('dietary_restrictions', child.medical_info.dietary_restrictions)
        child.medical_info.allergies = medical_info.get('allergies', child.medical_info.allergies)
        child.medical_info.medications = medical_info.get('medications', child.medical_info.medications)
        child.medical_info.special_needs = medical_info.get('special_needs', child.medical_info.special_needs)
        child.medical_info.notes = medical_info.get('notes', child.medical_info.notes)

        db.session.commit()
        return ChildSchema(exclude=['medical_info_id', 'emergency_contact']).dump(child)
    else:
        return {'error': 'Child not found'}, 404

@child_bp.route('/<int:child_id>/emergency_contact', methods=['PUT', 'PATCH'])
@jwt_required()
def update_child_emergency_contact(child_id):
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)
    emergency_contact = EmergencyContactSchema().load(request.json)

    if child:
        child.emergency_contact.first_name = emergency_contact.get('first_name', child.emergency_contact.first_name)
        child.emergency_contact.last_name = emergency_contact.get('last_name', child.emergency_contact.last_name)
        child.emergency_contact.relationship = emergency_contact.get('relationship', child.emergency_contact.relationship)
        child.emergency_contact.phone_number = emergency_contact.get('phone_number', child.emergency_contact.phone_number)
        child.emergency_contact.notes = emergency_contact.get('notes', child.emergency_contact.notes)

        db.session.commit()
        return ChildSchema(exclude=['emergency_contact_id', 'medical_info']).dump(child)
    else:
        return {'error': 'Child not found'}, 404


# Delete a child
@child_bp.route('/<int:child_id>', methods=['DELETE'])
@jwt_required()
def delete_child(child_id):
    # delete from child where id=child_id
    stmt = db.select(Child).filter_by(id=child_id)
    child = db.session.scalar(stmt)

    if child:
        db.session.delete(child)
        db.session.delete(child.medical_info)  # Delete corresponding medical information record
        db.session.delete(child.emergency_contact)  # Delete corresponding emergency contact record
        db.session.commit()
        return {"message": f"The records for child #{child.id} have been deleted."}, 200
    else:
        return {'error': 'Child not found'}, 404


