import random

from data.phrases import phrases
from src.print_functions import print_correctly
from src.user_input_functions import get_user_input, continue_to_ask_user_input

"""
    expression en anglais,
    liste des traductions possibles de l'expression en francais
"""

def quiz_phrase(expression, list_expressions) :

    user_input = ""

    if not(expression in phrases) :
        return

    list_phrases = {key: phrases[expression][key] for key in list_expressions
        if key in phrases[expression]}

    list_phrases = list(list_phrases.keys())
    phrases_about_expression = phrases[expression]

    while list_phrases and user_input != 'q':

        expression_fr = random.choice(list_phrases)
        print("Traduisez :")
        user_input = get_user_input("Votre réponse",
                                    phrases_about_expression[expression_fr]["question"])
        if user_input == 'q' :
            break

        elif user_input != 'n' :

            correct_answer = phrases_about_expression[expression_fr]["answer"]
            result = "[INCORRECTE]"
            if user_input == correct_answer :
                result = "[CORRECTE]"
                list_phrases.remove(expression)

            print(f"\n{result}\n\n\n")

            if result == "[INCORRECTE]" :
                input(print_correctly(f"Réponse : '{correct_answer}' :"))

        else :
            list_phrases.remove(expression)

        print("\n-----------------------------------------")
