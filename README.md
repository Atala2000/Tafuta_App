# TAFUTA APP

**Overview:**
Tafuta App is a streamlined solution designed to reunite lost items with their owners. It serves as a platform where users can effortlessly report lost items, fostering connections between lost belongings and their rightful owners.

## Components:

### 1. Front-end

**Technologies:**
- HTML5 and CSS
- Sass and Bootstrap
- jQuery

### 2. Back-end

**Technologies:**
- Python utilizing the Django framework for robust backend functionalities.
- Django Rest Framework for streamlined API development.

**Integration:**
The seamless connection between the front and back end is achieved through the implementation of a REST API.

## REST API:
**Django Framework**
The backend is developed using the Django framework, a high-level Python web framework known for its simplicity and scalability.
Utilizes Django's Model-View-Controller (MVC) architecture for efficient code organization and maintenance.
Implements well-defined endpoints that adhere to RESTful principles, ensuring a standardized and predictable API structure.
Leverages Django's built-in authentication and authorization mechanisms to secure API endpoints and manage user access.

**Django Rest Framework (DRF)**
Extends the capabilities of Django to facilitate the creation of RESTful APIs.
Serializers in DRF convert complex data types, such as Django models, into JSON representations for easy consumption by the front end.
Provides powerful class-based views for handling HTTP methods (GET, POST, PUT, DELETE) and responding with appropriate status codes.
Authentication classes in DRF allow for flexible and customizable authentication methods, ensuring data security.
Throttling, pagination, and filtering options in DRF enhance API performance and user experience.

**list of APIs**
items/ [name='item-list-create']
items/<int:pk>/ [name='item-retrieve-update-destroy']
electronics/ [name='electronics-list-create']
electronics/<int:pk>/ [name='electronics-retrieve-update-destroy']
credentials/ [name='credential-list-create']
credentials/<int:pk>/ [name='credentials-retrieve-update-destroy']
clothings/ [name='clothing-list-create']
clothings/<int:pk>/ [name='clothing-retrieve-update-destroy']
furniture/ [name='furniture-list-create']
furniture/<int:pk>/ [name='furniture-retrieve-update-destroy']
stationary/ [name='stationary-list-create']
stationary/<int:pk>/ [name='stationary-retrieve-update-destroy']
pets/ [name='pet-list-create']
pets/<int:pk>/ [name='pets-retrieve-update-destroy']
sign up/ [name='user-registration']
login/ [name='user-login']

**jQuery using Ajax**
Front-end interactions are facilitated through jQuery and Ajax, allowing asynchronous communication with the backend.
Executes GET requests to the defined API endpoints, retrieving JSON data from the Django backend.
Utilizes the retrieved data to dynamically populate the user interface, providing a seamless and responsive user experience.


## Running the Application:

Follow these steps to run the Tafuta App locally:

1. Clone the repository.
2. Navigate to the root folder.
3. Execute the command `python manage.py runserver`.
4. Open your browser and go to `localhost:8000`.
5. The application is now up and running.

## How to Use the Application:

1. The user-friendly interface allows users to effortlessly report lost items.
2. Users are prompted to provide details about the lost item for efficient tracking.
3. The application provides a convenient overview of all reported lost items.
4. Detailed information about a specific lost item is easily accessible to users.

Tafuta App simplifies the process of reporting and locating lost items, creating a user-centric experience for both reporting and searching for lost belongings.
