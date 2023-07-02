# R1. Identification of the problem you are trying to solve by building this particular app.

The childcare management system I am building as a Flask Web API will address the challenges and complexities associated with managing and organizing childcare centers effectively. The app seeks to streamline and automate various administrative tasks, ultimately enhancing the overall efficiency and quality of childcare services provided.

Due to scoping limitations I am only able to implement a small part of the functionality of a childcare management system. In this case it is the enrollment of children and registration of guardians (and other users) and the management this information.

Therefore the primary goal of the app (and the problem it is trying to solve) is to simplify the enrollment and registration process for children attending the childcare center. By capturing essential information and maintaining detailed records of children, parents/guardians, emergency contacts, medical information, and authorized pickups, the app ensures accurate and up-to-date information is readily available. This eliminates the need for manual paperwork and reduces the chances of errors or miscommunication.

The application also aims to provide information to interested parties (guardians and chldcare admins) and to allow such data to be viewed, updated and deleted based on whether they are a guardian, carer or childcare administrator.

This app solves the problem of managing a childcare center by automating the administrative and management side. It solves the problem of safe-guarding children and guardians by securing their data. The application offers centralized platform for managing crucial aspects of childcare operations. The app simplifies administrative tasks, reduces manual effort, minimizes errors, and enhances communication between parents/guardians, carers, and administrators. This ensures the well being and development of the children in their care.

# R2. Why is it a problem that needs solving?

The childcare management system I aim to develop as a Flask Web API addresses a significant problem faced by childcare centers and parents alike. The manual management of enrollment and registration,  can be tedious, time-consuming, error-prone, and inefficient. The chilcare management system leverages technology to automate and streamline this process.

The manual handling of enrollment and registration processes used to involve extensive paperwork, which can lead to errors, delays, and difficulties in maintaining accurate records. There is also the issue of losing such records in the event of fire or security issues, with anyone being able to doctor such records or gain unauthorized access.

By digitizing these processes and putting them online, the app eliminates paperwork, enables efficient data entry, and ensures that essential information about children, parents, guardians, emergency contacts, medical details, and authorized pickups is easily accessible and up to date.

Without such a system, staff would not be able to track the information about guardians and their children. They would not be able to track medical information or check whether the correct person is picking up the child which would imperil the child.

In addressing these problems through automation and digitization, the childcare management system brings efficiency, accuracy, and convenience to childcare centers and parents. It reduces administrative burden, improves communication, enhances child safety, and creates a smoother experience for all the users involved. 

# R3. Why have you chosen this database system. What are the drawbacks

By choosing PostgreSQL as the relational database management system my childcare management system, I  have considered its strengths and weaknesses in comparison to other database systems. The following outlines my reasons for choosing PostgreSQL and an overview of its pros and cons:

## Rationale for using PostgreSQL (Pros):

* Reliability and Stability: PostgreSQL is known for its reliability and stability, offering robust data integrity and ACID compliance. It ensures the consistency and durability of data, which is crucial for a childcare management system handling sensitive information.

* Advanced Features: PostgreSQL provides a wide range of advanced features, including support for complex queries, full-text search, spatial data, and JSON data types. These features can be beneficial when working with complex data structures or implementing specific functionalities in your system.

* Extensibility and Flexibility: PostgreSQL allows the creation of custom data types, functions, and extensions, offering flexibility in data modeling and application development. It supports multiple programming languages, making it suitable for integration with your Flask web API.

* Community Support: PostgreSQL has a large and active open-source community, providing continuous development, bug fixes, and security updates. The community-driven nature ensures a reliable and well-supported database system.

## Drawbacks of PostgreSQL (Cons):

* Learning Curve: Compared to some other database systems, PostgreSQL may have a steeper learning curve, especially for developers new to relational databases. Familiarizing yourself with its advanced features and SQL syntax might require additional effort.

* Memory Usage: PostgreSQL tends to utilize more memory compared to other database systems, particularly when handling large datasets or complex queries. Proper tuning and configuration may be required to optimize memory usage.

* Scale-Out Limitations: While PostgreSQL can handle sizable workloads, it may face challenges when scaling out horizontally across multiple servers compared to some distributed database systems. Scaling read-heavy workloads can require additional considerations.

* Complexity for Simple Applications: If your childcare management system has relatively simple data requirements and doesn't require advanced features, PostgreSQL's feature-rich nature might introduce unnecessary complexity.

PostgreSQL is a popular choice for relational database management due to its reliability, advanced features, extensibility, and strong community support. However, it requires a learning curve, consumes more memory, and might be overkill for simple applications. Evaluating your specific requirements, data complexity, and scalability needs can help determine if PostgreSQL is the right fit for your childcare management system.

# R4. Identify and discuss the key functionalities and benefits of an ORM

An ORM (Object Relational Mapper) is a software tool that enables developers to interact with a relational database using object-oriented programming (OOP) concepts. It acts as a bridge between the application's object model and the database, abstracting away the underlying database-specific operations and allowing developers to work with database entities as objects in their code.

Key Functionalities of an ORM:

* Object-Relational Mapping: The ORM maps database tables to object classes and provides mechanisms to perform CRUD (Create, Read, Update, Delete) operations on those objects. It handles the conversion between object-oriented code and relational database structures.

* Data Modeling: An ORM facilitates the creation of object-oriented models that represent the database schema. It allows developers to define relationships between objects, such as one-to-one, one-to-many, or many-to-many associations, and handles the translation of these relationships to relational database concepts.

* Query Generation and Optimization: An ORM provides a query language or API to interact with the database. It generates SQL queries based on high-level object-oriented operations and optimizes those queries for performance. This helps developers write database queries using familiar programming paradigms without worrying about the underlying SQL syntax or query optimization.

Benefits of Using an ORM:

* Productivity and Maintainability: By abstracting away the low-level database operations, an ORM simplifies the development process, reduces the amount of boilerplate code, and enhances code reusability. It allows developers to focus on the business logic of the application rather than database-specific details, improving productivity and maintainability.

* Portability and Database Independence: An ORM provides a database-agnostic interface, allowing developers to switch between different database systems (such as PostgreSQL, MySQL, SQLite) without rewriting the application code. This promotes flexibility and portability, enabling the application to be deployed on different environments easily.

* Security and Performance: Many ORMs incorporate security measures such as parameterized queries or query sanitization to prevent SQL injection attacks. They also offer query optimization techniques to improve performance by minimizing the number of database calls and optimizing data retrieval strategies.

* Abstraction of Complex Database Operations: ORMs handle complex database operations, such as joining tables, managing transactions, and handling concurrency issues, in a more abstract and intuitive manner. This simplifies the implementation of advanced database functionalities within the application.

Overall, an ORM simplifies database interactions, improves code organization, enhances productivity, and promotes maintainability and portability. It bridges the gap between object-oriented programming and relational databases, allowing developers to work with database entities as familiar objects and perform database operations using high-level, object-oriented constructs.

# R5. Document all endpoints for your API

## Enrollment and Registration:


- POST /auth/login

The childcare administrator must register a legal guardian first before they can register the children for that guardian.

Request Body

    { 
        "email": "jenna@spam.com",
        "password": "password123"
    }

Response Body

    {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODAxMzU3MywianRpIjoiZmMyYWM3NjEtOWE2NC00OGRmLTgxODQtZGFmZGRkYzU2NTM4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Implbm5hQHNwYW0uY29tIiwibmJmIjoxNjg4MDEzNTczLCJleHAiOjE2ODgwOTk5NzN9.rxQEo_LrFxmDooWHL--MaRmSbJDiRF9yKX_6LGgp7zE",
        "user": {
            "date_of_birth": "1969-02-14",
            "email": "jenna@spam.com",
            "first_name": "Jenna",
            "gender": "female",
            "id": 4,
            "last_name": "Walters",
            "phone_number": "0401548899",
            "role": {
                "id": 3,
                "role_desc": "The childcare center administrator",
                "role_name": "administrator"
            }
        }
    }

Response Body: When web token fails for any other route

    {
        "msg": "Signature verification failed"
    }

- GET /users: Get all user records

Request URI

http://localhost:5000/users

Response Body

    [
        {
            "date_of_birth": "1974-09-23",
            "email": "spam@spam.com",
            "first_name": "John",
            "gender": "male",
            "id": 1,
            "last_name": "Davies",
            "phone_number": "98885656",
            "role": {
                "id": 1,
                "role_desc": "The parent or legal guardian of the child",
                "role_name": "guardian"
            }
        },
        {
            "date_of_birth": "1976-04-03",
            "email": "tomato@spam.com",
            "first_name": "Joan",
            "gender": "female",
            "id": 2,
            "last_name": "Davies",
            "phone_number": "98885656",
            "role": {
                "id": 1,
                "role_desc": "The parent or legal guardian of the child",
                "role_name": "guardian"
            }
        } ...
    ]

- GET /users/<int: user_id>: get single user record

Request URI

http://localhost:5000/users/2

Response Body

    {
        "date_of_birth": "1976-04-03",
        "email": "tomato@spam.com",
        "first_name": "Joan",
        "gender": "female",
        "id": 2,
        "last_name": "Davies",
        "phone_number": "98885656",
        "role": {
            "id": 1,
            "role_desc": "The parent or legal guardian of the child",
            "role_name": "guardian"
        }
    }

- POST /users: Insert a new user record.

Request Body

{
	"date_of_birth": "1974-09-23",
	"email": "paul.briggs222@tpg.com.au",
	"password": "password123",
	"first_name": "Paul",
	"gender": "male",
	"last_name": "Briggs",
	"phone_number": "0400 561 216",
	"role_id": 3
}

Response Body

{
    "date_of_birth": "1974-09-23",
    "email": "paul.briggs222@tpg.com.au",
    "first_name": "Paul",
    "gender": "Male",
    "id": 8,
    "last_name": "Briggs",
    "password": "password123",
    "phone_number": "0400 561 216",
    "role": {
        "id": 3,
        "role_desc": "The childcare center administrator",
        "role_name": "administrator"
    }
}


http://localhost:5000/users/1

- POST /guardians: Insert a new parent/guardian record.

Request Body

    {
        "authorized_to_pickup": true,
        "medical_info_consent": true,
        "occupation": "Delivery Driver",
        "user": {
            "date_of_birth": "1984-10-12",
            "email": "joseph.parker@tpg.com.au",
            "password": "password123",
            "first_name": "Joseph",
            "gender": "male",
            "last_name": "Parker",
            "phone_number": "0400 181 797",
            "role_id": 1
        }
    }

Response Body

    {
        "authorized_to_pickup": true,
        "id": 4,
        "medical_info_consent": true,
        "occupation": "Delivery Driver",
        "user": {
            "date_of_birth": "1984-10-12",
            "email": "joseph.parker@tpg.com.au",
            "first_name": "Joseph",
            "gender": "male",
            "id": 6,
            "last_name": "Parker",
            "phone_number": "0400 181 797",
            "role": {
                "id": 1,
                "role_desc": "The parent or legal guardian of the child",
                "role_name": "guardian"
            }
        }
    }


- DELETE /users/<int: user_id>: Delete a child record.

Request URI

http://localhost:5000/users/1

Response Body

    {
        "message": "The records for user #1 - John Davies have been deleted."
    }

Rrequest URI

http://localhost:5000/guardians


GET /guardians: Retrieve all guardians.

Response Body

    [
        {
            "authorized_to_pickup": true,
            "id": 1,
            "medical_info_consent": true,
            "occupation": "Delivery Driver",
            "user": {
                "date_of_birth": "1974-09-23",
                "email": "spam@spam.com",
                "first_name": "John",
                "gender": "male",
                "id": 1,
                "last_name": "Davies",
                "phone_number": "98885656",
                "role": {
                    "id": 1,
                    "role_desc": "The parent or legal guardian of the child",
                    "role_name": "guardian"
                }
            }
        },
        {
            "authorized_to_pickup": true,
            "id": 2,
            "medical_info_consent": true,
            "occupation": "Software Engineer",
            "user": {
                "date_of_birth": "1976-04-03",
                "email": "tomato@spam.com",
                "first_name": "Joan",
                "gender": "female",
                "id": 2,
                "last_name": "Davies",
                "phone_number": "98885656",
                "role": {
                    "id": 1,
                    "role_desc": "The parent or legal guardian of the child",
                    "role_name": "guardian"
                }
            }
        },
        {
            "authorized_to_pickup": true,
            "id": 3,
            "medical_info_consent": true,
            "occupation": "Project Manager",
            "user": {
                "date_of_birth": "1984-11-19",
                "email": "amy.baron@gmail.com",
                "first_name": "Amy",
                "gender": "female",
                "id": 5,
                "last_name": "Baron",
                "phone_number": "0400 236 777",
                "role": {
                    "id": 1,
                    "role_desc": "The parent or legal guardian of the child",
                    "role_name": "guardian"
                }
            }
        }
    ]

- GET /guardians/<int: guardian_id>: Retrieve information about a specific guardian.

Request URI

http://localhost:5000/guardians/2

Response Body

    {
        "authorized_to_pickup": true,
        "id": 2,
        "medical_info_consent": true,
        "occupation": "Software Engineer",
        "user": {
            "date_of_birth": "1976-04-03",
            "email": "tomato@spam.com",
            "first_name": "Joan",
            "gender": "female",
            "id": 2,
            "last_name": "Davies",
            "phone_number": "98885656",
            "role_id": 1
        }
    }

- PUT/PATCH /guardians/<int: guardian_id>: Update the details of a parent/guardian.

Request body

    {
        "authorized_to_pickup": false,
        "medical_info_consent": true,
        "occupation": "Plumber"
    }

Response Body

    {
        "authorized_to_pickup": false,
        "id": 1,
        "medical_info_consent": true,
        "occupation": "Plumber",
        "user": {
            "date_of_birth": "1974-09-23",
            "email": "spam@spam.com",
            "first_name": "John",
            "gender": "male",
            "id": 1,
            "last_name": "Davies",
            "phone_number": "98885656",
            "role_id": 1
        }
    }

- DELETE /guardians/<int: guardian_id>: Delete a parent/guardian record.

Request URI

http://localhost:5000/guardians/3

Response Body

    {
        "message": "The records for guardian #3 have been deleted."
    }

A legal guardian can login and view information pertaining to their children.

- POST /children: Insert a new child record.

Request Body

    {
        "date_of_birth": "2020-07-11",
        "first_name": "Michael",
        "gender": "male",
        "last_name": "Mosely"
    }

Response Body

    {
        "date_of_birth": "2020-07-11",
        "emergency_contact_id": null,
        "first_name": "Michael",
        "gender": "male",
        "id": 5,
        "last_name": "Mosely",
        "medical_info_id": null
    }

- GET /children: Return all children

Request URI

http://localhost:5000/children

Response Body

    [
        {
            "date_of_birth": "2020-07-11",
            "emergency_contact_id": null,
            "first_name": "Anthony",
            "gender": "male",
            "id": 1,
            "last_name": "Punch",
            "medical_info_id": null
        },
        {
            "date_of_birth": "2019-03-12",
            "emergency_contact_id": null,
            "first_name": "Cloe",
            "gender": "female",
            "id": 2,
            "last_name": "Punch",
            "medical_info_id": null
        }
    ]

- GET /children/<int: child_id>: Retrieve information about a specific child.

Request URI

http://localhost:5000/children/2

Response Body

    {
        "date_of_birth": "2019-03-12",
        "emergency_contact_id": null,
        "first_name": "Cloe",
        "gender": "female",
        "id": 2,
        "last_name": "Punch",
        "medical_info_id": null
    }

- PUT/PATCH /children/<int: child_id>: Update the details of a child.

Request Body

    {
        "date_of_birth": "2020-07-11",
        "first_name": "Michael Jake",
        "gender": "male",
        "last_name": "Mosely"
    }

Response Body

    {
        "date_of_birth": "2020-07-11",
        "emergency_contact_id": null,
        "first_name": "Michael Jake",
        "gender": "male",
        "id": 3,
        "last_name": "Mosely",
        "medical_info_id": null
    }

- DELETE /children/<int: child_id>: Delete a child record.


Request URI

http://localhost:5000/children/3

Response Body

    {
        "message": "The records for child #3 have been deleted."
    }


GET /children/<int: child_id>/medical_info

Request URI

http://localhost:5000/children/8/medical_info

Response Body

    {
        "date_of_birth": "2016-07-11",
        "emergency_contact_id": null,
        "first_name": "Michael",
        "gender": "Male",
        "id": 8,
        "last_name": "Mosely",
        "medical_info": {
            "allergies": "",
            "dietary_restrictions": "",
            "id": 8,
            "medications": "",
            "notes": "",
            "special_needs": ""
        }
    }

PUT/PATCH /children/<int: child_id>/medical_info

Request URI

http://localhost:5000/children/7/medical_info

Request Body

    {
        "allergies": "dvfsdg",
        "dietary_restrictions": "fgdfg",
        "medications": "dfgdsg",
        "notes": "dfgdfd",
        "special_needs": "534346"
    }

Response Body

    {
        "date_of_birth": "2016-07-11",
        "emergency_contact_id": null,
        "first_name": "Michael",
        "gender": "Male",
        "id": 7,
        "last_name": "Mosely",
        "medical_info": {
            "allergies": "dvfsdg",
            "dietary_restrictions": "fgdfg",
            "id": 7,
            "medications": "dfgdsg",
            "notes": "dfgdfd",
            "special_needs": "534346"
        }
    }




GET /children/<int: child_id>/emergency_contact

Request URI

http://localhost:5000/children/2/emergency_contact

    {
        "date_of_birth": "2019-03-12",
        "emergency_contact": {
            "first_name": "John",
            "id": 2,
            "last_name": "Mecina",
            "notes": "Just some random text ...",
            "phone_number": "0401 856 715",
            "relationship": "Uncle"
        },
        "first_name": "Cloe",
        "gender": "female",
        "id": 2,
        "last_name": "Punch",
        "medical_info_id": 2
    }

PUT/PATCH /children/<int: child_id>/emergency_contact

Request Body

    {
        "first_name": "John",
        "last_name": "Mecina",
        "notes": "Just some random text ...",
        "phone_number": "0401 856 715",
        "relationship": "Uncle"
    }

Response Body

    {
        "date_of_birth": "2020-07-11",
        "emergency_contact": {
            "first_name": "John",
            "id": 1,
            "last_name": "Mecina",
            "notes": "Just some random text ...",
            "phone_number": "0401 856 715",
            "relationship": "Uncle"
        },
        "first_name": "Anthony",
        "gender": "male",
        "id": 1,
        "last_name": "Punch",
        "medical_info_id": 1
    }

GET /guardians_children: Returns the relationship that exists between guardians and their children

Request URI

http://localhost:5000/guardians_children

Response Body

    [
        {
            "child": {
                "date_of_birth": "2020-07-11",
                "first_name": "Anthony",
                "gender": "male",
                "id": 1,
                "last_name": "Punch"
            },
            "guardian": {
                "authorized_to_pickup": true,
                "id": 1,
                "medical_info_consent": true,
                "occupation": "Delivery Driver"
            },
            "id": 1
        },
        {
            "child": {
                "date_of_birth": "2020-07-11",
                "first_name": "Anthony",
                "gender": "male",
                "id": 1,
                "last_name": "Punch"
            },
            "guardian": {
                "authorized_to_pickup": true,
                "id": 2,
                "medical_info_consent": true,
                "occupation": "Software Engineer"
            },
            "id": 2
        }
    ]

GET /guardians_children/2: Returns one relationship that exists between a guardian and their child

Request URI

http://localhost:5000/guardians_children/2

Response Body

    {
        "child": {
            "date_of_birth": "2020-07-11",
            "first_name": "Anthony",
            "gender": "male",
            "id": 1,
            "last_name": "Punch"
        },
        "guardian": {
            "authorized_to_pickup": true,
            "id": 2,
            "medical_info_consent": true,
            "occupation": "Software Engineer"
        },
        "id": 2
    }

POST /guardians_children

Request Body

    {
        "guardian_id": 1,
        "child_id": 3, 
        "relationship_id": 1
    }

Response Body

    {
        "child": {
            "date_of_birth": "2019-10-16",
            "first_name": "Maisie",
            "gender": "female",
            "id": 3,
            "last_name": "Jones"
        },
        "guardian": {
            "authorized_to_pickup": true,
            "id": 1,
            "medical_info_consent": true,
            "occupation": "Delivery Driver",
            "user": {
                "date_of_birth": "1974-09-23",
                "email": "spam@spam.com",
                "first_name": "John",
                "gender": "male",
                "id": 1,
                "last_name": "Davies",
                "phone_number": "98885656",
                "role": {
                    "id": 1,
                    "role_desc": "The parent or legal guardian of the child",
                    "role_name": "guardian"
                },
                "role_id": 1
            }
        },
        "id": 5,
        "relationship": {
            "id": 1,
            "relationship_desc": "Parent of the child",
            "relationship_name": "Father"
        }
    }

PUT/PATCH /guardians_children/<int: guardians_children_id>: Update a single guardian-child relationship.

Request Body

    {
        "guardian_id": 1,
        "child_id": 3, 
        "relationship_id": 2
    }

Response Body

    {
        "child": {
            "date_of_birth": "2019-10-16",
            "first_name": "Maisie",
            "gender": "female",
            "id": 3,
            "last_name": "Jones"
        },
        "child_id": 3,
        "guardian": {
            "authorized_to_pickup": true,
            "id": 1,
            "medical_info_consent": true,
            "occupation": "Delivery Driver"
        },
        "guardian_id": 1,
        "id": 5,
        "relationship_id": 2
    }

DELETE /guardians_children/<int: guardians_children_id> : Delete a single guardian-child relationship.

Request URI

http://localhost:5000/guardians_children/5

Response Body

    {
        "message": "The records for guardian-child relationship #5 have been deleted."
    }


- POST /authorized-pickups: Insert a new authorized pickup record.
- GET /authorized-pickups/<int: pickup_id>: Retrieve information about a specific authorized pickup.
- PUT /authorized-pickups/<int: pickup_id>: Update the details of an authorized pickup.
- DELETE /authorized-pickups/<int: pickup_id>: Delete an authorized pickup record.

- POST /medical-information: Insert a new medical information record.
- GET /medical-information/<int: info_id>: Retrieve information about a specific medical information record.
- PUT /medical-information/<int: info_id>: Update the details of a medical information record.
- DELETE /medical-information/<int: info_id>: Delete a medical information record.

- POST /emergency-contacts: Insert a new emergency contact record.
- GET /emergency-contacts/<int: contact_id>: Retrieve information about a specific emergency contact.
- PUT /emergency-contacts/<int: contact_id>: Update the details of an emergency contact.
- DELETE /emergency-contacts/<int: contact_id>: Delete an emergency contact record.


## Attendance Tracking:
- POST /attendance: Record the arrival and departure times of a child.
- GET /attendance: Retrieve attendance records of all children.
- GET /attendance/<int: attendance_id>: Retrieve attendance records for a specific child.
- PUT /attendance/<int: attendance_id>: Update the attendance record of a child.
- DELETE /attendance/<int: attendance_id>: Delete an attendance record.

## Scheduling and Calendar Management:

- POST /schedule: Assign a task to a teacher/carer based on their availability and the schedule.
- GET /schedule/<int: schedule_id>: Retrieve information about a specific task.
- PUT /schedule/<int: schedule_id>: Update the details of a task.
- DELETE /schedule/<int: schedule_id>: Delete a task.

# R6. An ERD for your app

![Enrollment](docs/Enrollment%20and%20Registration.drawio.png)


# R7. Detail any third party services that your app will use

The following is a detailed description of third-party services used in the Chilcare Management System Web API and how they are used to record and manage data of users and children.

### SQLAlchemy

SQLAlchemy is a python ORM (Object-Relational Mapping) library that provides a high level interface to perform database operations on a relational database management system. SQLAlchemy is database independant, and can connect to MySQL or SQLite just as easily with the correct adapter/driver. In the childcare management system, SQLAlchemy will be used to define the database models for children, parents & guardians, emergency contacts and medical information. It facilitates the creation, retrieval, updating, and deletion of records in the database (CRUD operations), making it easier to manage and persist data. SQLAlchemy is supported in an application through the follwing import.

    from flask_sqlalchemy import SQLAlchemy

### Flask-marshmallow

Flask-marshmallow is a Flask integration layer of the Marshmallow library, which allows for easy serialization and deserialization of complex data objects to and from JSON. It integrates well with SQLAlchemy. In the childcare management system, flask-marshmallow will be used to define schemas for data models, such as children, guiardians, emergency contacts and medical information. It helps with data validation, input/output formatting, and serialization/deserialization of data between the API and clients. These are some sample imports that can be used from the flask-marshmallow library.

    from marshmallow import fields
    from marshmallow.validate import Length, And, Regexp
    from marshmallow.exceptions import ValidationError

### Python-dotenv

Python-dotenv is a package that enables the loading of environment variables from a ".env" file into a Flask application. In the childcare management system, python-dotenv will be utilized to store sensitive information like the database connection URI and json web token keys outside of the source code. This allows the developer to separate sensitive configuration information from the python code.

### Psycopg2

Psycopg2 is a PostgreSQL adapter for Python, that allows a python application to interface with a PostgreSQL driver to connect to PostgreSQL databases. Since PostgreSQL has been chosen as the database system for the childcare management system, psycopg2 will be used to establish connections, execute SQL queries, and handle database operations within the Flask Web API.

### Flask-Bcrypt

Flask-Bcrypt is a Flask extension that provides password hashing and verification capabilities using the bcrypt algorithm. In the childcare management system, Flask-Bcrypt will be used to securely store and verify passwords for parents, guardians, and carers. It helps protect sensitive user information by encrypting passwords before storing them in the database.

### Flask-JWT-Extended
Flask-JWT-Extended is a Flask extension that adds JSON Web Token (JWT) support to an application for authentication and access control during a session. In the childcare management system, Flask-JWT-Extended will be used to handle user authentication and generate secure JWTs (JSON Web Tokens) for authorized access to protected API endpoints. It helps ensure that only authenticated users can access and modify sensitive data, such as enrollment and medical information.

By utilizing these third-party services, the childcare management system Flask Web API has access to a full range of features and capabilities to run the web application securely and to tightly control access to protected information.

## Sources

https://www.sqlalchemy.org/

https://flask-marshmallow.readthedocs.io/en/latest/

https://betterdatascience.com/python-dotenv/

https://www.psycopg.org/docs/

https://flask-bcrypt.readthedocs.io/en/1.0.1/

https://4geeks.com/lesson/what-is-JWT-and-how-to-implement-with-Flask

# R8. Describe your projects models in terms of the relationships they have with each other

The following is an overview of the SQLAlchemy models and the relationships they have with each other. Each SQLAlchemy model represents an entity that maps directly to a table in the database. This models each entity (table) as objects in the flask application and simplifies interactions with the database. The  models are related to each other through the use of the db.ForeignKey() method and the db.relationship() method. 

The db.ForeignKey() method sets up foreign keys in a model and extablishes relationships between models based on the values in specific columns. The db.relationship() method defines a higher level relationship between 2 models and allows the data in a model being referenced by the foreign key to be embedded in its place when a query is performed throgh the ORM Child model. This is exemplified in the following json return:

    {
        "date_of_birth": "2020-07-11",
        "emergency_contact_id": 2,
        "first_name": "Anthony",
        "gender": "male",
        "id": 1,
        "last_name": "Punch",
        "medical_info": {
            "allergies": "",
            "dietary_restrictions": "",
            "id": 1,
            "medications": "",
            "notes": "",
            "special_needs": ""
        }
    }

This is the record of a child. Note that the medical information for this child is included (embedded) in the json dictionary instead of a medical_info_id. This is because a db.relationship was established between both models.

This is accomplished with the following statement defined in the Child model:

    emergency_contact =  db.relationship('EmergencyContact', back_populates='child')

And then specifying the following statement in the ChildSchema class which enables nesting of values in a JSON return.

class ChildSchema(ma.Schema):
    ...
    medical_info = fields.Nested('MedicalInformationSchema')
    ...

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'medical_info_id', 'medical_info', 'emergency_contact_id', 'emergency_contact')
        ordered=True

## Child Model

The Child model contains the information relating to the child entity like first_name, last_name, date_of_birth and gender. Each Child model is related to 2 other models (MedicalInformation and EmergencyContact). These models are related to the Child model through the following foreign key constraints declared in the Child model.

    medical_info_id = db.Column(db.Integer, db.ForeignKey('medical_information.id'))
    emergency_contact =  db.relationship('EmergencyContact', back_populates='child')


Relationships are established between the Child model and the models MedicalInformation and EmergencyContact with the following declarations.

    medical_info =  db.relationship('MedicalInformation', back_populates='child')
    emergency_contact =  db.relationship('EmergencyContact', back_populates='child')

Note that in both cases the 'back_populates' argument is the name of the variable declared in each of the other models (MedicalInformation and EmergencyContact), and this completes the relationship from the other end(s).

The Child model also has a relationship with the GuardianChild model. This is captured in the following manner.

    guardian_child = db.relationship('GuardianChild', back_populates='child', cascade='all, delete')


## Guardian Model

The Guardian model contains the information relating to the Guardian entity like first_name, last_name, occupation, etc. The Guardian model has a many-to-many relationship with 'Child' as a 'Child' can have more than one parent, and a parent can have more than one 'Child'. 

A  many-to-many relationship requires the creation of a join Model, GuardianChild in this instance. There is no foreign key constraint on GuardianChild, as tyhe Guardian exists as a foreign key in GuardianChild.

A relationship is established between the Guardian model and the GuardianChild model by declaring the following relationship.

    guardian_child = db.relationship('GuardianChild', back_populates='guardian', cascade='all, delete')

The 'back_populates' argument here refers to the variable guardian defined in GuardianChild.

The following line defined in GuardianSchema denotes the one-to-many relationship between the Guardian and GuardianChild models.

    guardian_child = fields.List(fields.Nested('GuardianChildSchema'))

The Guardian model is associated with a single unique User model, which contains the information common to all user types. A foreign key is required here.

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

A relationship between the Guardian and User models is also established.

    user = db.relationship('User', back_populates='guardian')

## GuardianChild Model

This model represents the join between the Child and Guardian model. This is established by declaring 2 foreign key constraints for each instance of the model.

    guardian_id = db.Column(db.Integer, db.ForeignKey('guardians.id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('children.id'), nullable=False)

Relationships between this model and the Child and Gurdian models are formed by declaring the following statements in GuadianChild.

    guardian = db.relationship('Guardian', back_populates='guardian_child')
    child = db.relationship('Child', back_populates='guardian_child')

Where 'guardian_child' is a variable declared in each Child and Guardian model instance.

The other foreign keys constraint declared in GuardianChild is relationship_id.

    relationship_id = db.Column(db.Integer, db.ForeignKey('relationships.id'))

GuardianChild references Relationship in order to characterise the association between Child and Guardian model instances. A relationship is established with the Relationship model.

    relationship = db.relationship('Relationship', back_populates='guardian_child')

## Relationship Model

The Relationship model has no foreign keys. It merely contains relationship types (e.g. Mother, Father, Sister, etc). However a relationship is declared to associate it back to the relationship variable in GuardianChild.

    guardian_child = db.relationship('GuardianChild', back_populates='relationship')

## User Model

The User model has one foreign key. It only contains role types (e.g. Mother, Father, Sister, etc). A relationship is declared to associate it back to the role variable in GuardianChild.

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

A relationship is declared to associate it back to the user variable in the model 'Role'.

    role = db.relationship('Role', back_populates='user')

## Role Model

The 'Role' model has no foreign keys. It merely contains role types (e.g. guardian, carer, childcare admin, etc). However a relationship is declared to associate it back to the role variable in User.

    user = db.relationship('User', back_populates='role')

## MedicalInformation Model

The 'MedicalInformation' model has no foreign keys. It maintains notes on allergies, medications, etc. However a relationship is declared to associate it back to the medical_info variable in Child.

    child = db.relationship('Child', back_populates='medical_info')

## EmergencyContact Model

The 'EmergencyContact' model has no foreign keys. It contains the contact details of the person to call in case of emergencies. However a relationship is declared to associate it back to the emergency_contact variable in Child.

    child = db.relationship('Child', back_populates='emergency_contact')


# R9. Discuss the database relations to be implemented in your application

This web api project represents a small subset of the functionality of a childcare management system. It aims to provide backend support for enrollment and registration. The following tables capture the informational requirements for this function:

* Children
* Guardians
* Guardians_Children
* Relationships
* Users
* Roles
* Medical_Information
* Emergency_Contacts

To be able to effectively access, traverse and maintain the integrity of this datbase the following database relations are required.

### One-to-Many Relationship: Children to Guardians

A one to many relationship is a type of cardinality where one entity is related to one or more other entities and where that collection of entities relates to only one entity. Strictly speaking a child in this system can have one or more guardians. A child can have a mother, or a mother and a father or an additional legal guardian like an agent from assigned from child services.

### One-to-Many Relationship: Guardians to Children

A one to many relationship also exists between guardians and children. One guardian can be associated with one or more children. As a business rule it makes the most sense to enroll at least one guardian at the beginning, and then enroll children associated with that gurdian. 

### Many-to-Many Relationship: Guardians to Children (Join Table)

The previous 2 senarios present a common problem. Both entities (guardians and children) effectively have a many-to-many relationship between them. Left on their own these two tables have the potential to create data redundancy and inconsistent behavior. The solution is to create a join table called guardians_children which serves to record the associations between each guardian and child. Each row in this table contains a foreign key to the child table and a foreign key to the guardian table. Each row or relationship has its own primary key so that each association is uniquely recorded and identified.

Once a guardian and child are created as entries in their respective tables, the system will associate them by making an entry into the guardians_children table. There are separate endpoints for insertion into this table.

At some point a user may want to delete a child or gaurdian individually. Deleting from either table will result in a referential integrity error, and the database software will prevent them from doing this. One senario where this can happen is if a parent has 2 children at the centre. One of the children is to be withdrawn upon reaching the age of maturity (6 years old). The other child is still young and will remain behind. To accomplish this safely the foreign keys (guardian_id and child_id) in the table defined with an ON CASCADE DELETE statement.

    FOREIGN KEY (child_id) REFERENCES children (child_id) ON DELETE CASCADE
    FOREIGN KEY (guardian_id) REFERENCES children (guardian_id) ON DELETE CASCADE

This means that when a user deletes a child, all references to that child in the guardians_children table will be deleted. This also applies a guadian is deleted. All references in guardians_children are removed.

### One-to-Many Relationship: Relationships to Guardians_Children (Join Table)

The guardians_children join table contains a field called relationship_id which is a foreign key referencing the relationship table. This foreign key is appropriately placed here to represent the relationship type between the guardian and child (Father, Mother, Maternal Aunt, etc). One guardian_child entry can only have one relationship type, but a relationship type can be used by many guardian/child pairings.


### One-to-Many Relationship: Users to Roles

The users table has a foreign key referencing the roles table. A role is either a guardian, carer or childcare administrator. All users of the system (for the purposes of this project) fall under one of these categories. A user can only have one role but a role can be used by many users. 

### One-to-One Relationship: Children to Medical Information

In the process of creating each child an entry is made into the medical_information table which contains no data. This table entry is later updated by guardians and staff members and acts as a permanent log of the childs medical information.

This entry is recorded as a foreign key in the child table and is a one-to-one relationship. One child is only ever associated with one medical information entry which contains the medical data for that specific child.

### One-to-One Relationship: Children to Emergency Contacts

Like in the previous example, the process of creating each child an entry is made into the emergency_contacts table which is also empty by default. This table entry is later updated by guardians and staff members and the point of contact for any emergencies.

This entry is recorded as a foreign key in the child table and is a one-to-one relationship. One child is only ever associated with one emergency_contact entry which contains the contact details of said person.

These database relations help establish the associations between the different entities in the childcare management system, enabling efficient storage and retrieval of information for enrollment, registration, and other operations.

### One-to-One Relationship: Guardians to Users

For the purposes of normalisation the information in the users entity was extracted out into its own table as it is information common to guardians, carers and childrcare administrators alike. So each user_id exists as a foreign key in other tables like guardians, which contains information spefic to guardians like their occupation or whether they are an authorized pickup. 

One guardian can only ever be associated with one user as they are the same individual.

# R10. Describe the way tasks are allocated and tracked in your project

I have settled on an Agile Kanban style approach to project management. I made the decision to create tasks based on individual coding milestones as well as the requirements for the readme document. Each card will represent a user story with each one containing tasks. Each card may or may not contain a README document requirement as they may coincide with a coding milestone, or they may be carried out independently and therefore be their own card.

The Trello board is divided into the following columns (a standard approach). All cards created will be initially placed in the Todo list and move into the "In Progress" column based on priority.

* Todo: Work that is yet to be commenced.
* In Progress: Work that is actively being undertaken.
* Review: Work that is completed and awaiting review. This may be a code review or it may be a requirement that is evaluated against the rubric criteria. If the item under review fails it is flagged and sent back to "In Progress".
* Completed: Work that is completely finished and had passed the review stage.

## User Stories

These user stories cover the main functionality of enrollment and registration, attendance tracking, and scheduling and calendar management in a childcare management system. They can serve as a starting point for designing and implementing the respective features of the RESTful web API for the childcare centre. It is from these stories that the tasks specified in my Trello board are derived. The User stories have been split off into broad categories as per my original web api proposal submitted on Discord. Stories appear beneath the category headings below:

### Enrollment and Registration:

1. As a childcare administrator, I want to be able to register a new child by providing their essential information such as name, date of birth, and contact details.

2. As a childcare administrator, I want to be able to maintain the records of children, parents/guardians, emergency contacts, medical information, and authorized pickups.

3. As a parent or guardian, I want to be able to update my child's information such as contact details or medical information.

4. As a childcare administrator, I want to be able to delete a child's record if they are no longer enrolled in the childcare center.

### Attendance Tracking:

1. As a childcare administrator, I want to be able to record the arrival and departure times of each child for accurate attendance tracking.

2. As a parent or guardian, I want to be able to view the attendance records of my child to keep track of their attendance history.

### Scheduling and Calendar Management:

1. As a childcare administrator, I want to be able to assign tasks to teachers or carers for each day, including activities like story hour, sleep, finger painting, lunch, etc.

2. As a teacher or carer, I want to be able to view my assigned tasks and the daily routines to plan and prepare accordingly.

3. As a childcare administrator, I want to be able to update or modify the assigned tasks and daily routines based on any changes or requirements.

4. As a parent or guardian, I want to be able to access the daily routines and tasks assigned to teachers or carers to stay informed about my child's activities.

![Enrollment](docs/trello-1.png)


![Attendence](docs/trello-2.png)


![Scheduling](docs/trello-3.png)


![Enrollment](docs/trello-4.png)


![Attendence](docs/trello-5.png)


![Scheduling](docs/trello-6.png)

