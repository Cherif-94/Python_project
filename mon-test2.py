class Voitures:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def afficher(self):
        print(f"Voiture : {self.marque} {self.modele}")

       

fruits = ["pomme", "banane", "orange"]

for fruit in fruits:
    print(fruit)


class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def afficher(self):
        print(f"{self.marque} {self.modele}")

# Liste d'objets
voitures = [
    Voiture("Toyota", "Corolla"),
    Voiture("BMW", "X5"),
    Voiture("Renault", "Clio")
]




# Création d'un objet
ma_voiture = Voitures("Toyota", "Corolla")

# Appel de méthode
ma_voiture.afficher()

# Itération sur une liste d'objets ( appel de méthode pour chaque objet dans une boucle )
for v in voitures:
    v.afficher()

# Itération sur une liste d'objets ( accès aux attributs directement )
for v in voitures:
    print(v.marque, v.modele)    