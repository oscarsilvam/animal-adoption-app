# :dog: Animal Adoption Web Application


A simple web application built with **Flask** allows users to add animals for adoption, browse available animals, and search through the database.

This project was developed as part of my learning journey in web development and backend programming.

## Features
- Add an animal
- Search animals
- Upload photos

## Technologies Used
- Python 3
- Flask
- SQLite
- Bootstrap
- JavaScript
- Jinja2
- HTML/CSS

## Project Structure
.
├── database.py     
├── db
│   └── animals.db    # SQLite database (ignored in Git)
├── main.py           # Flask application entry point
├── README.md
├── requirements.txt  # Python dependencies  
├── static
│   ├── css
│   │   └── style.css
│   ├── img
│   │   ├── animaux_present.PNG
│   │   └── pattes.png
│   ├── js
│   │   └── script_form_adoption.js
│   └── vendor
│       └── bootstrap
└── templates
    ├── animal.html
    ├── anim_recherche.html
    ├── base.html
    ├── form.html
    ├── homepage.html
    ├── partials
    │   └── _animals_grid.html
    ├── recherche.html
    └── selection.html


## Form Validation
- Client-side validation implemented in JavaScript
- Fields such as name, age, email, postal code, and photo format validated before submission
- Backend handles file upload security and data persistance

## NOTES
This project focuses on:

- Understanding Flask routing and templates
- Hnadling forms and file uploads
- Basic database operations
- Improving user experience with client-side validation

Future improvements could include:
- Backend validation
- Pagination
- REST API endpoints

