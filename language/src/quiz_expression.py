import random

from data.expressions import expressions
from src.quiz_phrase import quiz_phrase
from src.user_input_functions import get_user_input, continue_to_ask_user_input

def expression_chose_by_user(expression, user_input) :

    if user_input == "all" :
        return expression

    elif user_input == '?' :
        return [random.choice(expression)]

    indices = [int(number) - 1 for number in user_input.split(',')]
    expression_chose = [expression[index] for index in indices]
    return expression_chose


def quiz_expression() :

    list_expressions = list(expressions.keys())
    user_input = ""

    while list_expressions and user_input != 'q':

        expression = random.choice(list_expressions)
        print("Traduisez :")
        user_input = get_user_input("Votre réponse", expression)
        if user_input == 'q' :
            break

        elif user_input != 'n' :

            # correct_answer : liste des expressions en francais
            correct_answer = expressions[expression]["answer"]
            result = "[INCORRECTE]"
            if user_input in correct_answer :
                result = "[CORRECTE]"
                list_expressions.remove(expression)

            print(f"\n{result}\n\n\n"
            + f"Traductions possibles de '{expression}' :")

            user_input = get_user_input("Exercez vous", correct_answer, True)
            if user_input != 'n' and user_input != 'q' :
                quiz_phrase(expression,
                    expression_chose_by_user(correct_answer, user_input))

        else :
            list_expressions.remove(expression)

        print("\n-----------------------------------------")
