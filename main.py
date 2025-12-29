from flask import Flask, render_template, request, g, redirect, url_for
from database import Database
import random

app = Flask(__name__)

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


@app.route("/")
def index():
    list_animals = get_db().get_all_animaux()

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

@app.route("/animal/<int:id>")
def presentation_animal(id):
    animal = get_db().get_animal(id)

    return render_template("animal.html", animal=animal)

@app.route("/treatment_form", methods=["POST", "GET"])
def treatment_form():
    if request.method == "POST":
        
        #store form in data
        data = request.form

        name = data.get('nom')
        species = data.get('espece')
        breed = data.get('race')
        age = data.get('age')
        description = data.get('description')
        email = data.get('courriel')
        address = data.get('ad_civique')
        city = data.get('ville')
        post_code = data.get('c_postal')

        #Add the animal to the database
        add_animal = get_db().add_animal(name, species, breed, age, description, 
                                         email, address, city, post_code)   
            
        return render_template("animal.html", animal=add_animal)

    elif request.method == "GET":
        return redirect(url_for('index'))
    
@app.route("/recherche")
def search():
    val = request.args.get('recherche').strip()
    data = get_db().get_entry(val)
    
    return render_template('selection.html', animaux_select=data)    
    

            


    
  