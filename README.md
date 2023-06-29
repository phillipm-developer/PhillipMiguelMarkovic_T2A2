# R1. Identification of the problem you are trying to solve by building this particular app.

The childcare management system I am building as a Flask Web API will address the challenges and complexities associated with managing and organizing childcare centers effectively. The app seeks to streamline and automate various administrative tasks, ultimately enhancing the overall efficiency and quality of childcare services provided.

The primary goal of the app is to simplify the enrollment and registration process for children attending the childcare center. By capturing essential information and maintaining detailed records of children, parents/guardians, emergency contacts, medical information, and authorized pickups, the app ensures accurate and up-to-date information is readily available. This eliminates the need for manual paperwork and reduces the chances of errors or miscommunication.

Additionally, the app aims to streamline attendance tracking by recording arrival and departure times for each child. This not only ensures accurate attendance records but also provides valuable insights for both parents/guardians and childcare administrators regarding a child's attendance patterns and overall participation in the center's activities.

Moreover, the app assists in scheduling and calendar management by assigning tasks to teachers or carers based on their availability and preferences. This feature optimizes the utilization of resources, ensures proper coverage for various activities throughout the day (such as story hour, sleep, lunch, and finger painting), and facilitates efficient planning of daily routines.

By offering a centralized platform for managing crucial aspects of childcare operations, the app simplifies administrative tasks, reduces manual effort, minimizes errors, and enhances communication between parents/guardians, teachers, and administrators. Ultimately, the app aims to provide a seamless and organized childcare experience for all stakeholders involved, ensuring the well-being and development of the children in their care.

# R2. Why is it a problem that needs solving?

The childcare management system I aim to develop as a Flask Web API addresses a significant problem faced by childcare centers and parents alike. The manual management of enrollment and registration, attendance tracking, and scheduling tasks can be tedious, time-consuming, error-prone, and inefficient. By leveraging technology to automate and streamline these processes, the app aims to provide a solution that offers numerous benefits.

The manual handling of enrollment and registration processes used to involve extensive paperwork, which can lead to errors, delays, and difficulties in maintaining accurate records. There is also the issue of losing such records in the event of fire or security issues, with anyone being able to doctor such records.

By digitizing these processes and putting them online, the app eliminates paperwork, enables efficient data entry, and ensures that essential information about children, parents, guardians, emergency contacts, medical details, and authorized pickups is easily accessible and up to date.

Accurate attendance tracking is crucial for childcare centers to maintain accountability, ensure child safety, and generate reports for parents and regulatory compliance. Automating this process through the app simplifies attendance recording, reduces the chances of errors or omissions, and provides real-time access to attendance data for parents and administrators.

Scheduling and calendar management in a childcare center involves complex coordination of tasks, teachers' availability, and the needs of the children. The app's ability to assign tasks to teachers based on their availability and plan daily routines alleviates the manual effort required for scheduling, optimizes resource allocation, and ensures a well-organized and balanced routine for the children.

By addressing these challenges through automation and digitization, the childcare management system brings efficiency, accuracy, and convenience to childcare centers and parents. It reduces administrative burden, improves communication, enhances child safety, and creates a smoother experience for all the actors involved. Ultimately, the app aims to streamline operations, improve productivity, and provide a better childcare experience for both childcare providers and parents.

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
        "id": 3,
        "medical_info_consent": true,
        "occupation": "Delivery Driver",
        "user": {
            "date_of_birth": "1984-10-12",
            "email": "joseph.parker@tpg.com.au",
            "first_name": "Joseph",
            "gender": "male",
            "id": 5,
            "last_name": "Parker",
            "phone_number": "0400 181 797",
            "role_id": 1
        }
    }

Request URI

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
        "child_id": 3,
        "guardian": {
            "authorized_to_pickup": true,
            "id": 1,
            "medical_info_consent": true,
            "occupation": "Delivery Driver"
        },
        "guardian_id": 1,
        "id": 5,
        "relationship_id": 1
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

## Enrollment and Registration:

![Enrollment](docs/Enrollment%20and%20Registration.drawio.png)

## Attendance Tracking (Medical information and emergency contacts includeed here for convenience):

![Attendence](docs/Attendence%20Tracking.drawio.png)

## Scheduling and Calendar Management:

![Scheduling](docs/Scheduling%20and%20Calendar%20Management.drawio.png)



# R7. Detail any third party services that your app will use

The following is a detailed description of third-party services used the Chilcare Management System Web API and how they are used to carry out the functions specified in the user stories.

1. SQLAlchemy: SQLAlchemy is an ORM (Object-Relational Mapping) library that simplifies database operations by providing a high-level interface for interacting with relational databases. In the childcare management system, SQLAlchemy will be used to define the database models for children, parents & guardians, emergency contacts, medical information, authorized pickups, and schedules. It facilitates the creation, retrieval, updating, and deletion of records in the database (CRUD operations), making it easier to manage and persist data.

2. flask-marshmallow: flask-marshmallow is a Flask integration of the Marshmallow library, which allows for easy serialization and deserialization of complex data objects to and from JSON. In the childcare management system, flask-marshmallow will be used to define schemas for data models, such as children, parents, emergency contacts, and schedules. It helps with data validation, input/output formatting, and serialization/deserialization of data between the API and clients.

3. python-dotenv: python-dotenv is a package that enables the loading of environment variables from a ".env" file into a Flask application. In the childcare management system, python-dotenv will be utilized to store sensitive information like database credentials and API keys outside of the source code. It allows for easy configuration management and separation of sensitive information from the application code.

4. psycopg2: psycopg2 is a PostgreSQL adapter for Python, providing connectivity and interaction with PostgreSQL databases. Since you've chosen PostgreSQL as the database system for the childcare management system, psycopg2 will be used to establish connections, execute SQL queries, and handle database operations within the Flask Web API.

5. pip-review: pip-review is a package that assists in managing and updating Python packages installed in a project. It ensures that the project remains up-to-date with the latest package releases, including security patches and new features. In the childcare management system, pip-review will help to review outdated packages and upgrade them, ensuring the project's dependencies are up-to-date and secure.

6. Flask-Bcrypt: Flask-Bcrypt is a Flask extension that provides password hashing and verification capabilities using the bcrypt algorithm. In the childcare management system, Flask-Bcrypt will be used to securely store and verify passwords for parents, guardians, and carers. It helps protect sensitive user information by encrypting passwords before storing them in the database.

7. Flask-JWT-Extended: Flask-JWT-Extended is a Flask extension that adds JSON Web Token (JWT) support to an application for authentication and access control. In the childcare management system, Flask-JWT-Extended will be used to handle user authentication and generate secure JWTs for authorized access to protected API endpoints. It helps ensure that only authenticated users can access and modify sensitive data, such as enrollment information, attendance records, and schedules.

By utilizing these third-party services, the childcare management system Flask Web API benefits from streamlined database operations with SQLAlchemy, seamless data serialization and validation with flask-marshmallow, secure handling of sensitive information with python-dotenv, connectivity to the PostgreSQL database with psycopg2, efficient package management with pip-review, password security with Flask-Bcrypt, and authentication and access control with Flask-JWT-Extended. Together, these services provide essential functionalities and enhance the overall security and usability of the childcare management system.

# R8. Describe your projects models in terms of the relationships they have with each other

# R9. Discuss the database relations to be implemented in your application

There are 2 one to many relationships

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

