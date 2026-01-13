
const champVide = "Veuillez remplir ce champ avant de soummetre le formulaire";


function reinitMsgErreur() {
    document.querySelectorAll(".text-danger").forEach(err => err.textContent = "");
}

function valName() {
    const nameAnimal = document.getElementById("name").value.trim();

    if (!nameAnimal) {
        document.getElementById("err_name").innerHTML = champVide;
        return false;

        //If the animal's name is < 3 or > 20
    } else if (nameAnimal.length > 20 || nameAnimal.length < 3) {
        document.getElementById("err_name").innerHTML = "Le nom doit avoir entre 3"
            + " et 20 caractères";
        return false;
    }
    return true;
}

function valSpecies() {
    const speciesAnimal = document.getElementById("species").value.trim();

    if (!speciesAnimal) {
        document.getElementById("err_species").innerHTML = champVide;
        return false;
    }
    return true;
}

function valRace() {
    const raceAnimal = document.getElementById("race").value.trim();

    if (!raceAnimal) {
        document.getElementById("err_race").innerHTML = champVide;
        return false;
    }
    return true;
}

function valDescription() {
    const descrAnimal = document.getElementById("description").value.trim();

    if (!descrAnimal) {
        document.getElementById("err_description").innerHTML = champVide;
        return false;
    }
    return true;
}

function valAge() {
    const ageAnimString = document.getElementById("age").value.trim();
    const ageAnimal = Number(document.getElementById("age").value.trim());

    if (ageAnimString == null || ageAnimString === "") {
        document.getElementById("err_age").innerHTML = champVide;
        return false;

    } else if (ageAnimal < 0 || ageAnimal > 30) {
        document.getElementById("err_age").innerHTML = "L'âge doit être entre 0"
            + " et 30 ans";
        return false;
    }
    return true;
}

function valPhoto() {
    const inputPhoto = document.getElementById("photo");
    const file = inputPhoto.files[0];

    if(!file){
        document.getElementById("err_photo").innerHTML = champVide;
        return false;
    }

    const allowedTypes = ["image/png", "image/jpeg"];

    if(!allowedTypes.includes(file.type)){
        document.getElementById("err_photo").innerHTML = "Votre fichier doit être"
        + " au format .png, .jpg ou .jpeg";
        return false
    }
    return true;
}

function valEmail() {
    const email = document.getElementById("email").value.trim();

    if (!email) {
        document.getElementById("err_email").innerHTML = champVide;
        return false;
    }
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!regexEmail.test(email)) {
        document.getElementById("err_email").innerHTML = "Entrez un courriel valide";
        return false;
    }
    return true;
}

function valAddress() {
    const adrCivique = document.getElementById("address").value.trim();
    const city = document.getElementById("city").value.trim();
    const postCode = document.getElementById("post_code").value.trim().toUpperCase();


    if (!adrCivique) {
        document.getElementById("err_address").innerHTML = "Adresse incomplète!"
            + " Veuillez mettre une adresse civique";
        return false;
    }

    if (!city) {
        document.getElementById("err_city").innerHTML = "Adresse incomplète! "
            + "Veuillez mettre une ville";
        return false;
    }

    if (!postCode) {
        document.getElementById("err_post_code").innerHTML = "Adresse incomplète!"
            + " Veuillez mettre le code postal";
        return false;
    }

    const regexPostCode = /^[A-Za-z]\d[A-Za-z]\s?\d[A-Za-z]\d$/;


    if (!regexPostCode.test(postCode)) {
        document.getElementById("err_post_code").innerHTML = "Format de code "
            + "postal invalide. (Ex : H3T 1J5)";
        return false;
    }
    return true;
}

document.getElementById("form_adoption").addEventListener("submit", function (event) {

    reinitMsgErreur();

    //Call to all of functions
    const nameCheck = valName();
    const speciesCheck = valSpecies();
    const raceCheck = valRace();
    const ageCheck = valAge();
    const descrCheck = valDescription();
    const photoCheck = valPhoto();
    const emailCheck = valEmail();
    const addressCheck = valAddress();


    //If one of the called functions is false then preventDefault
    if (!nameCheck || !speciesCheck || !raceCheck || !ageCheck || !photoCheck ||
        !descrCheck || !emailCheck || !addressCheck) {
        event.preventDefault();
    }
})