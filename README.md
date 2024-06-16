# Online Store Inventory and Supplier Management API

## Overview

This project is designed to manage the inventory and suppliers for an online store. The system includes a RESTful API that handles the creation, retrieval, updating, and deletion of inventory items and suppliers. The API also manages the relationships between items and suppliers.

## Requirements

### Inventory Item Record
- Each item should have a name, a detailed description, a price, and the date when it was added to the inventory.

### Supplier Record
- Each supplier should have a name, contact information, and a list of items they supply.

### Inventory-Supplier Relationship
- An item can have one or multiple suppliers, and a supplier can provide multiple items.
- Employees should be able to view which suppliers provide a specific item and also see the list of items supplied by a particular supplier.

### Inventory Management
- Employees need capabilities to add, view, update, and remove items from the inventory.

### Supplier Management
- There should be functionalities to add new suppliers, update their details, and view their information.

### Data Accessibility
- Ensure that both inventory and supplier data are accessible in a format compatible with other systems (like web frontends or mobile applications).

### Testing and Documentation
- The system should be robust and accompanied by clear documentation for other developers and team members.

## Deliverables
- A working API that fulfills the above requirements, including handling relational data between inventory items and suppliers.
- Basic tests to verify the functionality and reliability of the API.
- Documentation for setting up the project and interacting with the API.

## API Documentation
API documentation can be accessed at [127.0.0.1:8000](http://127.0.0.1:8000/).

## Time Frame
Complete the task within 3 days.

## Evaluation Criteria
- **Understanding of Requirements**: Ability to interpret business needs and design a functional system with relational data models.
- **Functionality**: The API should accurately represent the relationships between inventory items and suppliers and perform all required operations.
- **Code Quality**: The code should be clean, efficient, and maintainable.
- **Documentation**: Provide clear and concise documentation for setup and usage of the API.

## Technology Used  
This project uses Django Rest Framework to manage the API and its interactions with the inventory and supplier data.
    
## Setup Commands
1. Create and Apply Migrations:  
  `python manage.py makemigrations`   
  `python manage.py migrate`

2. Create Employee Group and Permissions:  
  `python manage.py create_employee_group`  
  This custom management script located in the management/commands folder runs when the command is run, creating employee group and applying the necessary permissions.  

3. Run Server:  
  `python manage.py runserver`   
  Runs server on localhost, port 8000 (http://127.0.0.1:8000)   

## App directory  - inventory/
  ├── models.py - defines the models for inventory items and suppliers  
  ├── management  
  │   ├── commands  
  │       ├── create_employee_group_and_permissions
  ├── views.py - defines the views for the API  
  ├── serializers.py - defines the serializers for the API  
  ├── urls.py - defines the URLs for the API  
  ├── tests.py - defines the tests for the API  
  ├── requirements.txt - lists the dependencies for the project   
  └── README.md - this file  

The project directory inventory contains the following files:  
`models.py`: Defines the models for inventory items and suppliers.  
`create_employee_group_and_permission`s: A custom management tool to create an employee group and apply the necessary permissions.  
`views.py`: Defines the views for the API.  
`serializers.py`: Defines the serializers for the API.  
`urls.py`: Defines the URLs for the API.  
`tests.py`: Defines the tests for the API.  
`requirements.txt`: Lists the dependencies for the project.  

