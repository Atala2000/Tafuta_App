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

## List of APIs:
- [`items/` [name='item-list-create']](#)
- [`items/<int:pk>/` [name='item-retrieve-update-destroy']](#)
- [`category/` [name='category-list-create']](#)
- [`category/<int:pk>/` [name='category-retrieve-update-destroy']](#)
- [`electronics/items/` [name='electronics-item-list']](#)
- [`pets/items/` [name='pets-item-list']](#)
- [`credentials/items/` [name='credentials-item-list']](#)
- [`clothing/items/` [name='clothing-item-list']](#)
- [`stationary/items/` [name='stationary-item-list']](#)
- [`sign up/` [name='user-registration']](#)
- [`login/` [name='user-login']](#)
- [`logout/` [name='user-logout']](#)
- [`credentials/items/` [name='credentials-item-list']](#)


**jQuery using Ajax**
Front-end interactions are facilitated through jQuery and Ajax, allowing asynchronous communication with the backend.
Executes GET requests to the defined API endpoints, retrieving JSON data from the Django backend.
Utilizes the retrieved data to dynamically populate the user interface, providing a seamless and responsive user experience.

## Running the Application:

Follow these steps to run the Tafuta App locally:

1. Clone the repository.
2. Navigate to the root folder.
3. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```
4. Install the requirements:
   ```bash
   pip install -r requirement.txt
   ```
5. Execute the command:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and go to `localhost:8000`.
7. The application is now up and running.

## How to Use the Application:

1. The user-friendly interface allows users to effortlessly report lost items.
2. Users are prompted to provide details about the lost item for efficient tracking.
3. The application provides a convenient overview of all reported lost items.
4. Detailed information about a specific lost item is easily accessible to users.

Tafuta App simplifies the process of reporting and locating lost items, creating a user-centric experience for both reporting and searching for lost belongings.