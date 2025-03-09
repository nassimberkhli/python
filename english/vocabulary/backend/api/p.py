import re

def supprimer_caracteres_speciaux(chaine):
    # Supprimer tout ce qui est entre [] ou ()
    chaine_sans_caracteres = re.sub(r'\[.*?\]|\(.*?\)', '', chaine)
    return chaine_sans_caracteres

# Exemple d'utilisation
texte = "Voici un exemple [à enlever] avec des (parenthèses)."
resultat = supprimer_caracteres_speciaux(texte)
print(resultat)  # "Voici un exemple  avec des ."
