# Requirements Overview

This project uses the following Python packages, listed in `requirements.txt`. Below is a summary of each dependency and its purpose in the Martec Django web application.

---

## Frameworks

### `Django==5.2`
The primary web framework used to build the backend. Django provides URL routing, database ORM, views, and templating.

### `asgiref==3.8.1`
A required dependency of Django that provides ASGI (Asynchronous Server Gateway Interface) support, enabling async views and improved scalability.

### `sqlparse==0.5.3`
Used internally by Django to parse SQL queries for database inspection, debugging, and formatting.

---

## Media and Static Files

### `pillow==11.2.1`
Python Imaging Library fork used to handle and validate uploaded images in the `Products` model (JPEG, PNG support).

---

## Deployment & Hosting

### `dj-database-url==2.3.0`
Helps configure Django database settings from a single `DATABASE_URL` environment variable. Essential for 12-factor apps and Heroku deployment.

### `gunicorn==23.0.0`
A production-grade WSGI HTTP server for running Django apps. Often used when deploying to platforms like Heroku or DigitalOcean.

---

## Environment Management

### `python-dotenv==1.1.0`
Loads environment variables from a `.env` file. Useful for keeping secrets and config (e.g. database credentials, debug mode) outside of source code.

---

## Utilities

### `packaging==25.0`
Used by some packages (such as `gunicorn`) to parse version strings and handle Python packaging standards.

### `typing_extensions==4.13.2`
Backports newer type hinting features for compatibility. Required by some dependencies for full typing support in newer Python versions.

---

## Notes

- These packages are managed inside a Python virtual environment and listed in `requirements.txt`.
- Use `pip install -r requirements.txt` to install all dependencies.
- This project is compatible with **Python 3**.
