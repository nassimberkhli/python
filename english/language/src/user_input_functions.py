import re

from src.print_functions import format_, print_help

def number_is_in_expression(expression_chose, size) :

    for number in expression_chose :

        if int(number) - 1 < 0 or size < int(number) - 1 :
            return False

    return True

def continue_to_ask_user_input(user_input, isForPhrases, correct_expression_fr) :

    if user_input == 'h' or (len(user_input) > 0 and user_input[-1] == ',') :
        return True;

    elif user_input == 'n' or user_input == 'q' :
        return False

    elif not(isForPhrases) :
        return False

    elif re.match(r"^(\d+)(,\d+)*$", user_input) :

        if number_is_in_expression(user_input.split(','), len(correct_expression_fr) - 1) :
            return False

        print()
        if len(user_input.split(',')) > 1 :
            input(f"{user_input} ne font pas partie de la liste ")
        else :
            input(f"{user_input} ne fait pas partie de la liste ")

    elif user_input == "all" or user_input == '?' :
        return False

    else :
        print()
        input(f"Mauvais pattern : '{user_input}'")

    return True;

def ask_user_input(request, input_string) :

    print(f"\n{format_(input_string)}")
    return input(f"\n{request} (help 'h') : ").strip().lower()

def get_user_input(request, specific_request, isForPhrases = False) :

    user_input = ask_user_input(request, specific_request)

    while continue_to_ask_user_input(user_input, isForPhrases, specific_request) :

        if user_input == 'h' :
            print_help(isForPhrases)

        user_input = ask_user_input(request, specific_request)

    return user_input
