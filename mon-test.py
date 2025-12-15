# Ce petit script affiche un message et fait une addition simple

def Bienvenue(nom):


    return f"Bonjour {nom}, bienvenue dans Python !"


def addition(a, b):
    """Fonction qui fait une addition"""
    return a + b

def pair (n):
    """Fonction qui vérifie si un nombre est pair"""
    return n % 2 == 0

def multiplier(a, b):
    """Fonction qui fait une multiplication"""
    return a * b 


def compter_voyelles(phrase):
    voyelles = "aeiouyAEIOUY"
    compteur = 0
    for char in phrase:
        if char in voyelles:
            compteur += 1
    return compteur



# Exécution du script

if __name__ == "__main__":

    n = 4
    if pair(n):
        print(f"{n} est un nombre pair.")
    else:
  
      print(f"{n} est un nombre impair.")


    nom = "Cherif"
    print(Bienvenue(nom)) # le print affiche le retour de la fonction saluer



    resultat = addition(5, 7)
    print(f"Le résultat de 5 + 7 est : {resultat}")

    resultat2 = multiplier(3, 4)
    print(f"Le résultat de 3 * 4 est : {resultat2}")

    phrase = "Bonjour tout le monde"  # le type de la variable est une chaîne de caractères
    nb_voyelles = compter_voyelles(phrase)
    print(f"La phrase '{phrase}' contient {nb_voyelles} voyelles.")