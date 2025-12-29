
const champVide = "Veuillez remplir ce champ avant de soummetre le formulaire";

//Reinitialiser les erreurs a une chaine vide
function reinitMsgErreur() {
    document.querySelectorAll(".text-danger").forEach(err => err.textContent = "");
}

function valNom() {
    const nomAnimal = document.getElementById("nom").value.trim();

    if (!nomAnimal) {
        document.getElementById("err_nom").innerHTML = champVide;
        return false;

        //Si la longueur du nom de l'animal est < 3 ou > 30
    } else if (nomAnimal.length > 20 || nomAnimal.length < 3) {
        document.getElementById("err_nom").innerHTML = "Le nom doit avoir entre 3"
            + " et 20 caractères";
        return false;
    }
    return true;
}

function valEspece() {
    const especeAnimal = document.getElementById("espece").value.trim();

    if (!especeAnimal) {
        document.getElementById("err_espece").innerHTML = champVide;
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

function valEmail() {
    const courriel = document.getElementById("courriel").value.trim();

    if (!courriel) {
        document.getElementById("err_courriel").innerHTML = champVide;
        return false;
    }
    const regexCourriel = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!regexCourriel.test(courriel)) {
        document.getElementById("err_courriel").innerHTML = "Entrez un courriel valide";
        return false;
    }
    return true;
}

function valAdresse() {
    const adrCivique = document.getElementById("ad_civique").value.trim();
    const ville = document.getElementById("ville").value.trim();
    const codePostal = document.getElementById("c_postal").value.trim().toUpperCase();
    

    if (!adrCivique) {
        document.getElementById("err_ad_civique").innerHTML = "Adresse incomplète!"
            + " Veuillez mettre une adresse civique";
        return false;
    }

    if (!ville) {
        document.getElementById("err_ville").innerHTML = "Adresse incomplète! "
            + "Veuillez mettre une ville";
        return false;
    }

    if (!codePostal) {
        document.getElementById("err_code_postal").innerHTML = "Adresse incomplète!"
            + " Veuillez mettre le code postal";
        return false;
    }

    const regexCodePostal = /^[A-Za-z]\d[A-Za-z]\s?\d[A-Za-z]\d$/;
    

    if (!regexCodePostal.test(codePostal)) {
        document.getElementById("err_code_postal").innerHTML = "Format de code "
            + "postal invalide. (Ex : H3T 1J5)";
        return false;
    }
    return true;
}

document.getElementsByTagName("form")[0].addEventListener("submit", function (event) {

    reinitMsgErreur();

    //Appeler toutes les fonctions
    const nomCheck = valNom();
    const especeCheck = valEspece();
    const raceCheck = valRace();
    const ageCheck = valAge();
    const descrCheck = valDescription();
    const emailCheck = valEmail();
    const adresseCheck = valAdresse();


    if (!nomCheck || !especeCheck || !raceCheck || !ageCheck || !descrCheck
        || !emailCheck || !adresseCheck) {
        event.preventDefault();
    }
})