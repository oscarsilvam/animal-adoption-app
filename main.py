from flask import Flask, render_template, request, g, redirect, url_for
from database import Database
import random
import os
from werkzeug.utils import secure_filename
import uuid

#Folder that will containt the photos added by users
UPLOAD_FOLDER = os.path.join("static", "uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Creation of the animals table
with app.app_context():
    db = Database()
    db.connect()
    db.add_table_animals()

def get_db():
    if 'db' not in g:
        g.db = Database()
        g.db.connect()
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()    

#check if the filename is secure
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    list_animals = get_db().get_all_animals()

    if len(list_animals) > 0:
        nbr = min(5, len(list_animals))

        #Choose 5 animals from the list
        chosen_anim = random.sample(list_animals, nbr)
    else:
        chosen_anim =[]    

    return render_template("homepage.html", animaux=chosen_anim)


@app.route("/formulaire")
def form_animal():
    return render_template("form.html")

#Renders the animal.html page for the animal with the given ID.
@app.route("/animal/<int:id>")
def presentation_animal(id):
    animal = get_db().get_animal(id)

    return render_template("animal.html", animal=animal)


@app.route("/treatment_form", methods=["POST", "GET"])
def treatment_form():
    if request.method == "POST":
        
        #store form in data
        data = request.form

        name = data.get('name')
        species = data.get('species')
        breed = data.get('race')
        age = data.get('age')
        description = data.get('description')
        email = data.get('email')
        address = data.get('address')
        city = data.get('city')
        post_code = data.get('post_code')
        
        file_photo = request.files.get('photo')
        photo = None
        if file_photo and file_photo.filename and allowed_file(file_photo.filename):
            ext = file_photo.filename.rsplit('.', 1)[1].lower()
            photo = f"{uuid.uuid4().hex}.{ext}"
            file_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo))
        
        #Add the animal to the database
        add_animal = get_db().add_animal(photo, name, species, breed, age, description, 
                                         email, address, city, post_code)   
            
        return render_template("animal.html", animal=add_animal, photo=photo)

    elif request.method == "GET":
        return redirect(url_for('index'))
    
@app.route("/recherche")
def search():
    val = request.args.get('recherche').strip()
    data = get_db().get_entry(val)
    
    return render_template('selection.html', animaux_select=data)    
