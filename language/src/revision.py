import random

from backend import wordreference as wr
from src.print_functions import format_
from src.user_input_functions import get_user_input

def find_a_translation(user_word, user_input, translations) :

    all_meanings = set()
    # print(translations)
    for key, translation in translations[0].items() :

        if isinstance(translation, dict) :

            if translation["word"].split(" [")[0] == user_word :
                all_meanings.update(translation["meanings"])

                if user_input in translation["meanings"] :
                    return list()

    return list(all_meanings)

def load_user_words(file_path='backend/data/user_words.txt'):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
        return []

def revision(specefic_meanings = []) :

    user_words = load_user_words()
    if not user_words:
        print("Aucune user_word à tester.")
        return

    user_input = ""
    specefic_meanings = []

    while user_words and user_input != 'q':

        user_word = random.choice(user_words)
        translations = wr.fetch_translation(user_word, "enfr", specefic_meanings)

        if not translations:
            print(f"Aucune traduction trouvée pour l'user_word : '{user_word}'")
            user_words.remove(user_word)
            continue

        user_input = get_user_input("Votre réponse", user_word)

        if user_input == 'q':
            break

        elif user_input != 'n' :

            result = find_a_translation(user_word, user_input, translations)
            if len(result) == 0 :
                user_words.remove(user_word)
                print(f"\n[CORRECTE]\n")
            else :
                input(f"\n[INCORRECTE] Traduction possible :\n")
                input(format_(result))

        else :
            user_words.remove(user_word)

        print("\n-----------------------------------------")

