import random
import textwrap

from rules import rules
from phrases import phrases

def quiz():
    remaining_phrases = list(phrases.keys())
    continu = '\n'

    while remaining_phrases and continu != "stop":

        # Sélectionner une phrase aléatoire parmi celles restantes
        phrase_fr = random.choice(remaining_phrases)

        # Afficher la phrase en français à traduire
        print(f"Traduisez cette phrase:\n\n{textwrap.fill(phrase_fr, width=40)}")
        user_input = input("\n\nVotre réponse (relancer ',' / arrêter 'stop'): ")

        if (user_input == "stop")
            break;

        # Permettre à l'utilisateur de corriger sa réponse si nécessaire
        while len(user_input) > 0 and user_input[-1] == ',':
            print(f"Traduisez cette phrase:\n\n{textwrap.fill(phrase_fr, width=40)}")
            user_input = input("\n\nVotre réponse (relancer ','): ")

        # Ajouter un point si la réponse ne se termine pas par un point
        if len(user_input) > 1:
            if user_input[-1] != '.':
                user_input += '.'

        # Comparer la réponse de l'utilisateur avec la bonne traduction
        if user_input.strip().lower() == phrases[phrase_fr]["answer"].strip().lower():
            print("\n[TRUE]")
            remaining_phrases.remove(phrase_fr)
        else:
            print(f"\n[FALSE] :\n\n{textwrap.fill(phrases[phrase_fr]['answer'], width=40)}")
            # Afficher la règle associée à la phrase incorrecte
            print(f"\n{phrases[phrase_fr]['rule']} : {textwrap.fill(rules[phrases[phrase_fr]['rule']], width=40)}")
            continu = input("\nVotre réponse était correcte ? y/n|*/stop : ")
            if continu == 'y':
                remaining_phrases.remove(phrase_fr)

        print("\n----------------")

    if len(remaining_phrases) == 0:
        print("[CONGRATULATION] !!!")

quiz()

