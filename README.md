# :dog: Animal Adoption Web Application


A simple web application built with Flask that allows users to add animals for adoption, browse available animals, and search through the database.

This project was developed as part of my learning journey in web development and backend programming.

## :bulb: Features
- Add an animal for adoption via a form
- Search animals by keyword
- Upload an image for each animal
- Client-side form validation with JavaScript
- Persistent storage using SQLite
- Responsive UI built with Bootstrap

## :hammer: Technologies Used
- Python 3
- Flask
- SQLite
- Bootstrap
- JavaScript
- Jinja2
- HTML/CSS

## :file_folder: Project Structure

```text
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

```    


## :mag_right: Form Validation
- Client-side validation implemented in JavaScript
- Fields such as name, age, email, postal code, and photo format validated before submission
- Backend handles file upload security and data persistance

## :blue_book: NOTES
This project focuses on:

- Understanding Flask routing and templates
- Handling forms and file uploads
- Basic database operations
- Improving user experience with client-side validation

## :telescope: Future improvements could include:
- Backend validation
- Pagination
- REST API endpoints

## :bust_in_silhouette: Author

Oscar Silva
Software Development Student

