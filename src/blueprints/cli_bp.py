from flask import Blueprint
from datetime import date, datetime
from models.user import User
from models.role import Role
from models.guardian import Guardian
from models.child import Child
from models.relationship import Relationship
from models.guardian_child import GuardianChild
from models.medical_information import MedicalInformation
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

    db.session.query(Role).delete()
    db.session.add_all(roles)
    db.session.commit()

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

    db.session.query(Relationship).delete()
    db.session.add_all(relationships)
    db.session.commit()

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
        ),
        User(
            first_name = 'Amy',
            last_name = 'Baron',    
            email = 'amy.baron@gmail.com',
            password = bcrypt.generate_password_hash('password123').decode('utf8'),
            phone_number = '0400 236 777',
            date_of_birth = '1984-11-19',
            gender = 'female',
            role_id = 1
        )
    ]

    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

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
        ),
        Guardian(
            user_id = 5,
            occupation = "Project Manager",
            medical_info_consent = True,
            authorized_to_pickup = True
        )
    ]

    db.session.query(Guardian).delete()
    db.session.add_all(guardians)
    db.session.commit()

    medical_info_list = [
        MedicalInformation(
            dietary_restrictions ="",
            allergies ="",
            medications ="",
            special_needs ="",
            notes =""
        ),
        MedicalInformation(
            dietary_restrictions ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ...",
            allergies ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ...",
            medications ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ...",
            special_needs ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ...",
            notes ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ..."
        ),
        MedicalInformation(
            dietary_restrictions ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ...",
            allergies ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ...",
            medications ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ...",
            special_needs ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ...",
            notes ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ..."
        )
    ]    

    db.session.query(MedicalInformation).delete()
    db.session.add_all(medical_info_list)
    db.session.commit()

    emergency_contact_list = [
        EmergencyContact(
            first_name = "",
            last_name = "",
            relationship = "",
            phone_number = "",
            notes = ""
        ),
        EmergencyContact(
            first_name = "John",
            last_name = "Mecina",
            relationship = "Uncle",
            phone_number = "0401 856 715",
            notes = "Just some random text ..."
        ),
        EmergencyContact(
            first_name = "Angela",
            last_name = "Robbins",
            relationship = "Maternal Aunt",
            phone_number = "0400 201 655",
            notes = "Just some random text ..."
        )
        
    ]

    db.session.query(EmergencyContact).delete()
    db.session.add_all(emergency_contact_list)
    db.session.commit()

    children = [
        Child(
            first_name = "Anthony",
            last_name = "Punch",
            date_of_birth = "2020-07-11",
            gender = "male",
            medical_info_id = 1,
            emergency_contact_id = 1
        ),
        Child(
            first_name = "Cloe",
            last_name = "Punch",
            date_of_birth = "2019-03-12",
            gender = "female",
            medical_info_id = 2,
            emergency_contact_id = 2
        ),
        Child(
            first_name = "Maisie",
            last_name = "Jones",
            date_of_birth = "2019-10-16",
            gender = "female",
            medical_info_id = 3,
            emergency_contact_id = 3
        )
    ]

    db.session.query(Child).delete()
    db.session.add_all(children)
    db.session.commit()

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

    db.session.query(GuardianChild).delete()
    db.session.add_all(guardians_children)
    db.session.commit()

    print('Models seeded')
