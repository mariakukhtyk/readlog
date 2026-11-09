# Readlog 
#### Video Demo:(https://youtu.be/1G9j-G8urVQ)
#### Description: 
# ReadLog

#### Video Demo:  

#### Description:

ReadLog is a minimalist, modern full-stack web application built to help users seamlessly organize, track, and manage their personal reading journeys. Designed with a strong emphasis on clean aesthetics, responsive user experience, and robust software architecture, the platform provides a distraction-free digital space to catalog books across custom reading statuses—such as Want to Read, Currently Reading, and Completed. Developed using Python, Flask, SQLite, Bootstrap 5, and Jinja2, ReadLog bridges intuitive frontend UI/UX design with secure backend data handling.

### Architectural Overview & Design Choices

When building ReadLog, several key architectural and design choices were made to ensure security, maintainability, and user experience. Rather than storing plaintext passwords, user registration utilizes Werkzeug security for cryptographic password hashing combined with salting. Session management via Flask session ensures that private library routes are strictly protected against unauthorized access.

The SQLite database is structured around relational integrity using users and books tables linked by foreign keys. Strict schema constraints like NOT NULL rules and unique index checks on usernames prevent orphaned records and duplicate entries, while parameterized SQL queries protect the application against SQL injection vulnerabilities. Inspired by modern minimalism, the user interface relies on Bootstrap 5 utility classes, custom CSS styling, soft component borders, and contextual status badges. Every layout choice was intentionally kept clean to ensure the focus remains entirely on the user's book collection rather than interface clutter.

### Main Backend Script (`app.py`)

This is the core Python backend script for the Flask application. It initializes the app configuration, establishes connection rules to the SQLite database, and defines all HTTP route handlers for GET and POST requests. It manages user session states for login and logout, processes registration form submissions with password hashing validation, handles database queries for CRUD operations on books, and includes custom helper decorators for route authorization.

### Dependency Manifest (`requirements.txt`)

This standard manifest file lists all required Python third-party packages for the project environment—including Flask, Werkzeug, and the CS50 library—ensuring reproducible installation across different machines and environments.

### Database Schema (`schema.sql`)

This file contains the foundational SQL DDL statements used to create the relational database tables for users and books. It defines column datatypes, primary keys, foreign key constraints, and unique indexes required to maintain data integrity across user sessions and book entries.

### Master Layout (`templates/layout.html`)

This master layout template is written in HTML5 and Jinja2. It establishes the global HTML skeleton, imports Bootstrap 5 stylesheets and navigation scripts, and implements dynamic block inheritance for body content. It also includes flash message rendering logic to display real-time feedback alerts, such as success or error notifications, across user actions.

### Main Dashboard (`templates/index.html`)

This is the primary dashboard view rendered after a user logs in. It queries the database for the current user's library and dynamically renders book cards using Jinja2 loops. It showcases individual book titles, authors, page counts, and interactive status badges within a responsive grid layout.

### User Authentication Views (`templates/login.html` and `templates/register.html`)

The login template serves as the authentication entry point featuring a clean, centered form card to collect user credentials and submit them via a secure POST request to the backend validation route. The registration template provides form fields for username creation, password entry, and password confirmation, guiding new users straight into the automatic login and dashboard redirection pipeline upon successful validation.

### Library Management & Error Handling (`templates/add.html` and `templates/apology.html`)

The add template enables users to input new book details—including title, author, total page count, and initial reading status—before dispatching the payload to the server for database insertion. The apology template is a dedicated error-handling view designed to render user-friendly error messages and HTTP status codes whenever form validation fails or unauthorized actions are attempted.

### Custom Styling (`static/styles.css`)

This custom stylesheet complements Bootstrap 5 by defining specific aesthetic enhancements. It includes custom typography scaling, card hover transitions, soft component border styling, and color palettes tailored to maintain the application's signature minimalist look.