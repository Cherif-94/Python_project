def saluer(nom):

    return f"Bonjour {nom}, bienvenue dans Python !"

def calcul(a,b) : 

    return a + b # le retour de la fonction ca sera la somme de a et b 


# Exécution du script

if __name__ == "__main__":
    
    nom = "Bréval"
    print(saluer(nom)) 

    a = 10 
    b = 20

    resultat = calcul(a, b)  ; 
    print(f"La somme  est : {resultat}") # le print affiche le retour de la fonction addition 
    
    
    # le print affiche le retour de la fonction saluer