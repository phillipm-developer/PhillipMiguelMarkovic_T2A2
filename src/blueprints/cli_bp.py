from flask import Blueprint
from datetime import date, datetime
from models.user import User
from models.role import Role
from models.guardian import Guardian
from models.child import Child
from models.relationship import Relationship
from models.guardian_child import GuardianChild
from models.authorized_pickup import AuthorizedPickup
from models.attendance import Attendance
from models.attendance_status import AttendanceStatus
from models.emergency_contact import EmergencyContact

from init import db, bcrypt

cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')

@cli_bp.cli.command('seed')
def seed_db(): 
    roles = [
        Role(
            role_name = 'guardian',
            role_desc = 'The parent or legal guardian of the child'
        ),
        Role(
            role_name = 'carer',
            role_desc = 'The primary carer of the child in the centre'
        ),
        Role(
            role_name = 'administrator',
            role_desc = 'The childcare center administrator'
        )
    ]

    relationships = [
        Relationship(
            relationship_name = 'Father',
            relationship_desc = 'Parent of the child'
        ),
        Relationship(
            relationship_name = 'Mother',
            relationship_desc = 'Parent of the child'
        ),
        Relationship(
            relationship_name = 'Paternal Uncle',
            relationship_desc = 'Uncle of the child'
        ),
        Relationship(
            relationship_name = 'Paternal Aunt',
            relationship_desc = 'Aunt of the child'
        ),
        Relationship(
            relationship_name = 'Maternal Uncle',
            relationship_desc = 'Uncle of the child'
        ),
        Relationship(
            relationship_name = 'Maternal Aunt',
            relationship_desc = 'Aunt of the child'
        )
    ]

    users = [
        User(
            first_name = 'John',
            last_name = 'Davies',    
            email = 'spam@spam.com',
            password = bcrypt.generate_password_hash('password123').decode('utf8'),
            phone_number = '98885656',
            date_of_birth = '1974-09-23',
            gender = 'male',
            role_id = 1
        ),
        User(
            first_name = 'Joan',
            last_name = 'Davies',    
            email = 'tomato@spam.com',
            password = bcrypt.generate_password_hash('password123').decode('utf8'),
            phone_number = '98885656',
            date_of_birth = '1976-04-03',
            gender = 'female',
            role_id = 1
        ),
        User(
            first_name = 'Penny',
            last_name = 'Smith',    
            email = 'penny@spam.com',
            password = bcrypt.generate_password_hash('password123').decode('utf8'),
            phone_number = '0400556699',
            date_of_birth = '1966-05-25',
            gender = 'female',
            role_id = 2
        ),
        User(
            first_name = 'Jenna',
            last_name = 'Walters',    
            email = 'jenna@spam.com',
            password = bcrypt.generate_password_hash('password123').decode('utf8'),
            phone_number = '0401548899',
            date_of_birth = '1969-02-14',
            gender = 'female',
            role_id = 3
        )
    ]

    guardians = [
        Guardian(
            user_id = 1,
            occupation = "Delivery Driver",
            medical_info_consent = True,
            authorized_to_pickup = True
        ),
        Guardian(
            user_id = 2,
            occupation = "Software Engineer",
            medical_info_consent = True,
            authorized_to_pickup = True
        )
    ]

    children = [
        Child(
            first_name = "Anthony",
            last_name = "Punch",
            date_of_birth = "2020-07-11",
            gender = "male"
        ),
        Child(
            first_name = "Cloe",
            last_name = "Punch",
            date_of_birth = "2019-03-12",
            gender = "female"
        )
    ]

    guardians_children = [
        GuardianChild(
            guardian_id = 1,
            child_id = 1,
            relationship_id = 1
        ),
        GuardianChild(
            guardian_id = 2,
            child_id = 1,
            relationship_id = 2
        ),
        GuardianChild(
            guardian_id = 1,
            child_id = 2,
            relationship_id = 1
        ),
        GuardianChild(
            guardian_id = 2,
            child_id = 2,
            relationship_id = 2
        )
    ]

    authorized_pickups = [
        AuthorizedPickup(
            child_id = 1,
            first_name = 'Mark',
            last_name = 'Davies',
            relationship_id = 3
        )
    ]

    # Truncate the authorized pickups table
    db.session.query(AuthorizedPickup).delete()
    # Truncate the guardians_children table
    db.session.query(GuardianChild).delete()
    # Truncate the Children table
    db.session.query(Child).delete()
    # Truncate the User table
    db.session.query(Guardian).delete()
    # Truncate the User table
    db.session.query(User).delete()
    # Truncate the Role table
    db.session.query(Role).delete()
    # Truncate the relationships table
    db.session.query(Relationship).delete()

    db.session.query(AttendanceStatus).delete()

    # Add the card to the session (transaction)
    # db.session.add(card)
    db.session.add_all(guardians)
    db.session.add_all(users)
    db.session.add_all(roles)
    db.session.add_all(relationships)
    db.session.add_all(children)
    db.session.add_all(guardians_children)
    db.session.add_all(authorized_pickups)

    attendance_statuses = [
        AttendanceStatus(
            status_name = 'Awaiting Arrival',
            status_desc = 'Awaiting arrival of the child'
        ),
        AttendanceStatus(
            status_name = 'Absent',
            status_desc = 'Did not arrive within designated timeframe'
        ),
        AttendanceStatus(
            status_name = 'Picked Up',
            status_desc = 'Picked up by guardian or authorized pickup'
        )
    ]

    attendances = [
        Attendance(
            child_id = 1,
            date = date.today(),
            arrival_time = datetime.now().strftime("%H:%M:%S"),
            departure_time = datetime.now().strftime("%H:%M:%S"),
            status_id = 1
        ),
        Attendance(
            child_id = 2,
            date = date.today(),
            arrival_time = datetime.now().strftime("%H:%M:%S"),
            departure_time = datetime.now().strftime("%H:%M:%S"),
            status_id = 1
        )
    ]


    emergency_contacts = [
        EmergencyContact(
            first_name = 'Mark',
            last_name = 'Davies',
            relationship_id = 3,
            phone_number = '0400 516 999',
            notes = 'Uncle of the child'
        )
    ]

    # Truncate the attendances pickups table
    db.session.query(Attendance).delete()
    # Truncate the attendance_statuses table
    db.session.query(AttendanceStatus).delete()
    # Truncate the emergency contacts table
    db.session.query(EmergencyContact).delete()

    db.session.add_all(attendance_statuses)
    db.session.add_all(attendances)
    db.session.add_all(emergency_contacts)

    # Commit the tranaction to the database
    db.session.commit()
    print('Models seeded')
