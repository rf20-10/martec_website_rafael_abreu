# Design

This file describes the overall design decisions behind the Martec Concrete Products Website. The goal of this document is to explain the architectural structure, user flow, and key trade-offs made during the development of the site using Django.

---

## Objectives

- Build a bilingual-friendly (Portuguese for Brazilian audience and english to present this project) responsive website for a family owned concrete products company.
- Offer an intuitive and simple UX with minimal dependencies.
- Support future extensibility (e.g., CRM integration, admin product control).
- Ensure accent insensitive search for the brazilian users.

---

## System Architecture

This is a standard Django project with a single app (`martec`). The backend handles routing, template rendering, and form processing. Static assets (CSS, JavaScript, images) are served from the `/static/` directory and are enhanced using Bootstrap 5 for responsiveness and consistency.

---

## Component Overview

### Models

Defined in `models.py`:

- `User`: Inherits from `AbstractUser` — extensible for future roles (e.g., sales admin).
- `Products`: Contains name, description, image (optional), and timestamps. Uses `ImageField` for product photos and supports null for flexibility.
- `Contact_Form`: Stores submitted contact form entries. Useful for CRM and admin review.

**Design Justification:**

- Nullable `ImageField` allows for easy data entry without forcing complete records.
- Timestamps (`created_at`, `updated_at`) help with product update history.
- Form fields like email and phone use `CharField` to accommodate varying input formats.

---

### Views and Routing

Defined in `views.py` and `urls.py`:

- Each view corresponds to a public-facing page: `index`, `products`, `about_us`, and `contact`.
- The `contact` view contains inline form logic and feedback status tracking.

**Design Justification:**

- URL names use Portuguese (`produtos`, `sobre_nos`...) to better support customers.
- Contact form errors are customized in Portuguese for UX clarity.
- Toast notifications implemented client side to avoid page reloads and give fast feedback to end user.

---

### Templates

Structured using Django’s templating system. All pages extend from a shared `layout.html` for consistency.

#### `layout.html`

Includes the site’s Bootstrap navbar, footer, and main structure.

#### `index.html`

Simple hero section with call to action to contact via sales department of the business via WhatsApp.

#### `products.html`

- Lists products in responsive cards.
- Search bar at the top allows for JavaScript based, diacritic insensitive search.

**Design Justification:**

- Search is handled client side to reduce server load and to ensure fast results.
- Diacritic insensitivity ensures usability in Portuguese regardless of keyboard settings.

#### `about_us.html`

Static page with the company’s history, values, and testimonials.

#### `contact.html`

Contains a styled Django form with validation and user feedback.

**Design Justification:**

- Toast feedback avoids page refreshes and keeps the user informed in real time.
- Contact data is stored in the database for future automation (such as email replies, and/or CRM sync).

---

## Static Assets

### `styles.css`

- Customizes Bootstrap defaults to reflect brand identity.
- Ensures consistent padding, layout spacing, and responsive grid alignment.

### `script.js`

- Implements:
  - Diacritic insensitive search.
  - Toast message display based on form status.
  - Smooth scrolling for enhanced UX.

**Design Justification:**

- Pure JavaScript was used to avoid jQuery or other dependencies, keeping bundle size low.
- Modular functions (`removeDiacritics`, `showToast`) enhance clarity and testability.

---

## Security Considerations

- CSRF tokens are included in forms using Django’s `{% csrf_token %}` tag.
- Form input is validated on both client (HTML5) and server (Django form validation) levels.
- No authentication was implemented as this is a public-facing website; however, `User` model is in place for future admin functionality.

---

## Extensibility

This design allows for future enhancements such as:

- Admin dashboard for managing products and viewing contact submissions.
- WhatsApp API integration for form replies.
- Language toggle for English/Portuguese.

---

## Known Limitations

- No image resizing or optimization beyond Pillow’s validation.
- Form submissions are stored but not emailed or alerted in real time.

---

## Summary

The Martec website delivers a clean, accessible interface for showcasing products and capturing customer interest. Design decisions prioritize user experience, responsiveness, and a localized (Portuguese first) approach, while keeping the codebase extensible and maintainable.
