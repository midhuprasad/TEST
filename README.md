# Login and Registration System

This project is a simple login and registration system built using Django. It allows users to register for a new account, log in with their credentials, and view their home page.

## Features

- User registration: Users can create a new account by providing their username, email, password, and confirming the password.
- User login: Registered users can log in with their username and password.
- Home page: After successful login, users are directed to a home page.

## Installation

1. Clone the repository:

git clone <repository_url>

2. Create a virtual environment:

python -m venv env

3. Activate the virtual environment:

  source env/bin/activate

4. Install the dependencies:

pip install -r requirements.txt

5. Run the migrations:

python manage.py migrate

6. Start the development server:

python manage.py runserver

7. Access the application at [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

- Register a new account:
- Access the registration page at [http://localhost:8000/register](http://localhost:8000/register).
- Fill in the registration form with your desired username, email, password, and confirm the password.
- Click the "Register" button to create your account.
- Log in to an existing account:
- Access the login page at [http://localhost:8000/Login](http://localhost:8000/Login).
- Enter your username and password in the login form.
- Click the "Login" button to log in.
- Home page:
- After successful login, you will be directed to your home page.
- You can view and interact with the content on your home page.
