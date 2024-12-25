# User-Authentication-Django-
# Project Overview

This project is a web application built using Django (version 5.1.4) that provides user authentication and a dashboard interface. The application utilizes several third-party packages, including `django-crispy-forms` for enhanced form rendering and `crispy-bootstrap5` for styling.

## Features

- **User Registration**: Users can create an account using a registration form.
- **User Login**: Users can log in to their accounts using their credentials.
- **Dashboard**: After logging in, users are redirected to a dashboard page.
- **Home Page**: A public home page is available for all users.
- **Logout**: Users can log out and return to the home page.

## File Structure

- **`requirements.txt`**: Lists the dependencies required for the project, including Django and form styling packages.
- **`main/urls.py`**: Contains the URL routing for the application, mapping URLs to their corresponding views.
- **`main/views.py`**: Defines the view functions that handle requests and render the appropriate templates.
- **`main/templates/auth/`**: Contains HTML templates for user authentication, including login, registration, and dashboard pages.

## URL Configuration

The following URLs are configured in the application:

- `/home/`: Renders the home page.
- `/register/`: Displays the registration form and handles user registration.
- `/login/`: Displays the login form and handles user authentication.
- `/dashboard/`: Renders the user dashboard after successful login.
- `/logout/`: Logs the user out and redirects to the home page.

## Getting Started

To get started with the project, ensure you have Python and Django installed. You can install the required packages using:

```bash
pip install -r requirements.txt
```

Run the development server with:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/home/` to access the application.
