# Martec Concrete Products Website

This is a website I built using Django for Martec, a concrete products company based in Piedade-SP, Brazil. It’s a family-owned business (owned by my family), and the goal of this project was to provide them with a simple, responsive, and professional web presence. The entire interface is in Portuguese and tailored to a Brazilian audience. The code and project structure are in English. To test the UI in English, you can use translation tools like Google Translate, as demonstrated in the YouTube video.

# Video presentation
https://www.youtube.com/watch?v=T4Uhu7e23pY

## Overview

The website includes:
- A homepage with a brief introduction of the business and a WhatsApp link to contact the sales department.
- A products page listing all offerings, featuring an accent insensitive search (important in the Portuguese language).
- An "About Us" page describing the company’s mission and values.
- A contact page with a validated form and toast-style feedback messages using Bootstrap.

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap 5), JavaScript
- **Image Handling:** Pillow

## How to Run the Project Locally

1. Clone the Repository from GitHub  
   Open a terminal and run:  
   ```bash
    git clone https://github.com/rf20-10/martec_website_rafael_abreu.git
   cd martec_website_rafael_abreu  
2. Create and activate a virtual environment:  
   **Linux/macOS:**  
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```  
   **Windows:**  
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
4. Apply migrations:  
   ```bash
   python manage.py migrate
   ```  
5. Start the development server:  
   ```bash
   python manage.py runserver
   ```  
6. Open your browser and go to:  
   `http://127.0.0.1:8000`

## Project Structure Overview
```
martec/
├── requirements.txt
├── requirements-overview.md
├── README.md
├── design.md
├── martec/
│   ├── static/martec/
│   │   ├── script.js
│   │   ├── styles.css
│   │   └── images/
│   ├── templates/martec/
│   │   ├── layout.html
│   │   ├── index.html
│   │   ├── about_us.html
│   │   ├── products.html
│   │   └── contact.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── ...
├── final_project/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
```

## Dependencies
```
Listed in `requirements.txt`:  
-asgiref==3.8.1
-dj-database-url==2.3.0
-Django==5.2
-gunicorn==23.0.0
-packaging==25.0
-pillow==11.2.1
-psycopg2-binary==2.9.10
-python-dotenv==1.1.0
-sqlparse==0.5.3
-typing_extensions==4.13.2
```

# Project Overview
```
## views.py

This file contains the core views handling user-facing pages:

- `index()`: Renders the homepage.
- `products()`: Fetches and displays all product entries from the database.
- `about_us()`: Static view to display company background.
- `contact()`: Dynamically renders and validates a contact form. Error messages and labels are customized in Portuguese to enhance user experience. A form status is passed to the template to trigger feedback via toast.

**Design Choices:**

- Form class is defined inside the view for modularity and separation from global scope.
- Form fields have Bootstrap styling via widgets for a consistent UI.
- Clear feedback to users using form validation and `form_status`.

---

## urls.py

Defines the app-specific URL routes:

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("produtos/", views.products, name="products"),
    path("sobre_nos/", views.about_us, name="about_us"),
    path("contato/", views.contact, name="contact"),
]

**Design Choices:**

- URLs use Portuguese keywords (produtos, sobre_nos, etc.) to better support customers.

## models.py

Defines the data structure:

- **User**: Custom user model (inherits from Django’s `AbstractUser`) for future extensibility.
- **Products**: Represents the products with name, image, description.
- **Contact_Form**: Represents user submitted contact inquiries with validation fields.

**Design Choices:**

- `ImageField` used for product visuals; `null=True` and `blank=True` to allow flexibility.
- `created_at` and `updated_at` enable product tracking and admin history.
- Phone field allows for variable input formats (with country codes or dashes).

---

## apps.py

Standard Django configuration class for the `martec` app.

---

## Templates

### layout.html

Base template using Bootstrap 5, with consistent layout, navbar, and footer. Other pages extend this.

**Design Choices:**

- Mobile-responsive with proper titles and structure.

### index.html

Landing page with hero section and featured image.

**Design Choices:**

- hero section for the prospect accessing the website to have a quick call to action to contact the sales department for a quote

---

### products.html

Displays product cards using a responsive Bootstrap grid. A client-side search allows users to filter products by name.

**Design Choices:**

- Fallback image included if product image is null.
- Search implemented in JavaScript with diacritic insensitive matching for better user support in portuguese.

---

### about_us.html

Static content about the company with structured sections (hero, image + text, values, testimonial).

---

### contact.html

Dynamic contact form with validation and toast notification feedback.

**Design Choices:**

- Form fields styled with `is-invalid` classes for instant user feedback.
- Data stored via the model for persistence (in the future to support email replies, and/or CRM sync).
- Contact info and business hours displayed.

---

## Static Files

### styles.css

Custom CSS for branding and layout:

- Enforces image ratios.
- Custom button colors.
- Better spacing and responsive design for different sections.

---

### script.js

Handles client-side search and toast display:

- `removeDiacritics()`: Ensures search works without accents (essential for Portuguese).
- `scrollToProduct()`: Smoothly scrolls to the product that matches search input.
- `showToast()`: Dynamically updates and displays success/error messages.

**Design Choices:**

- Vanilla JavaScript instead of external libraries to reduce dependencies.
- User focused experience


## Final notes
Pillow is a Python additional package used for image processing in the products.html page. For more information, visit requirements.md file.
```
