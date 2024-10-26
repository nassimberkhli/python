import textwrap

def format_(input_string) :

    if isinstance(input_string, str) :
        return textwrap.fill(input_string, width=40)

    elif isinstance(input_string, list) :
        return '\n'.join(
            f"{i+1} - {textwrap.fill(s, width=40)}"
            for i, s in enumerate(input_string))


def print_help(isForPhrases) :

    input("\n"
        + " - '*' 0 ou 1 ou plusieurs caractères\n"
        + " - '*,' relancer\n"
        + " - 'n' refuser\n"
        + " - 'q' quitter\n")

    if isForPhrases :
        print(" - '[1-n]' choisir un/des chiffres, exemple : '1,3'\n"
        + " - '?' au hasard\n"
        + " - 'all' tout\n")
