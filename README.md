# Flask Social-Blogging App
This repository contains a Flask-based social-blogging application that allows users to register, create posts, edit posts, comment on posts, and more. 
The project is built using best practices outlined in the book [Flask Web Development: Developing Web Applications with Python](https://www.oreilly.com/library/view/flask-web-development/9781491991725/).

## Features
**User Registration**: Users can create accounts and receive email notifications about their registration.
**Post Creation**: Users can create and publish their own blog posts.
**Post Editing**: Users have the ability to edit their existing posts.
**Commenting**: Users can engage with posts by leaving comments.
**User Roles**: The application has different roles including Admin, Moderator, and Users, each with distinct permissions for various actions.
**Environment Setup**: The project supports three environments: test, dev, and prod.
**Testing**: The repository includes a comprehensive test suite that thoroughly tests each module of the application, as well as front-end testing with Selenium.
**Database Manipulation**: The project utilizes the SQLAlchemy ORM for efficient and seamless database manipulation.

## Installation
To run the application locally, follow these steps:

1. Clone the repository:

        git clone https://github.com/mbvyn/social-blogging-app.git
  
2. Install the required dependencies:

        pip install -r requirements.txt
        
3. Run the application:

        export FLASK_APP=manage.py
        
        flask run
        
4. Open your web browser and visit http://localhost:5000 to access the application.


## Contributing
Contributions to this project are welcome. 
If you find any bugs or have suggestions for new features, please open an issue or submit a pull request. Make sure to follow the established coding style and guidelines.

## Acknowledgments
The development of this application was inspired by the insights and guidance provided in the book [Flask Web Development: Developing Web Applications with Python](https://www.oreilly.com/library/view/flask-web-development/9781491991725/).
