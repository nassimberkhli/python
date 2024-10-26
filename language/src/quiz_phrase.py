import random
from backend.wordreference import get_examples
from src.user_input_functions import get_user_input
from src.print_functions import print_correctly

def quiz_phrase(expression, translations):
    user_input = ""

    for key, sub_dict in translations.items() :

        if len(sub_dict["examples"]) > 1 :

            translate = sub_dict["examples"][1]

            print("Traduisez :")
            user_input = get_user_input("Votre réponse", example_fr)
            if user_input == 'q':
                break

            result = "[INCORRECTE]"
            if user_input == correct_answer:
                result = "[CORRECTE]"
                examples.remove((example_fr, correct_answer))

            print(f"\n{result}\n")
            if result == "[INCORRECTE]":
                input(print_correctly(f"Réponse : '{correct_answer}'"))

            print("\n-----------------------------------------")
