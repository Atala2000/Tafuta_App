# TAFUTA APP
The application is a simple solution meant to connect lost items with their users. It provides an interface where lost items can be reported and give a platform for their owners to connect with them

## The application is split into two 
1. Front-end
## Technologies
1. HTML5 and CSS
2. Sass and Bootstrap 
3. jQuery

2. Back-end
## Technologies
1. Python using Django framework for the backend

The front and backend are connected through the use of a REST API
## REST API
1. Django framework defines endpoints that return JSON representation of data stored in a database
2. jQuery using Ajax makes a GET request to the endpoint and uses the data returned to populate 

## How to run the application
1. Clone the repository
2. Navigate to the root folder
3. Run the command `python manage.py runserver`
4. Open the browser and navigate to localhost:8000
5. The application should be running

## How to use the application
1. The application has a simple interface that allows users to report lost items
2. The user is required to fill in the details of the lost item
3. The user can also view the lost items that have been reported
4. The user can also view the details of the lost item