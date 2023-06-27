from flask import Blueprint
from datetime import date
from models.user import User
from models.role import Role
from models.guardian import Guardian
from models.child import Child
from models.relationships import Relationship
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

    # Add the card to the session (transaction)
    # db.session.add(card)
    db.session.add_all(guardians)
    db.session.add_all(users)
    db.session.add_all(roles)
    db.session.add_all(relationships)
    db.session.add_all(children)

    # Commit the tranaction to the database
    db.session.commit()
    print('Models seeded')
