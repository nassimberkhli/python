import random
import re

from backend import wordreference as wr
from src.print_functions import format_
from src.user_input_functions import get_user_input

def good_translation(user_input, meanings) :

    # print(meanings)
    if len(user_input) == 0 :
        return False

    for meaning in meanings:
        # print(meaning)
        cleaned_meaning = re.sub(r' \[.*?\]| \(.*?\)|\+ *($| )', '', meaning)
        
        if user_input == cleaned_meaning:
            return True
    
    return False

def find_a_translation(user_word, user_input, translations) :

    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    all_meanings = set()
    # print(translations)
    for key, translation in translations[0].items() :

        if isinstance(translation, dict) :

            if translation["word"][0].split(" [")[0] == user_word :
                all_meanings.update(flatten(translation["meanings"]))

                if good_translation(user_input, list(all_meanings)) :
                    return list()

    return list(all_meanings)

def load_user_words(file_path='backend/data/user_words.txt'):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
        return []

def get_word(raw_word) :

    match = re.match(r"([a-zA-Z ]+)([0-9 ]*)", raw_word)
    
    if match:
        user_word = match.group(1).strip()
        specific_meanings = list(map(int, match.group(2).split())) if match.group(2).strip() else []
    else:
        user_word = None
        specific_meanings = []
    
    return user_word, specific_meanings, raw_word

def revision(specefic_meanings = []) :

    user_words = load_user_words()
    if not user_words:
        print("Aucune user_word à tester.")
        return

    user_input = ""
    specefic_meanings = []

    while user_words and user_input != 'q' :

        user_word, specefic_meanings, raw_word = get_word(random.choice(user_words))
        translations = wr.fetch_translation(user_word, "enfr", specefic_meanings)

        if not translations :
            print(f"Aucune traduction trouvée pour l'user_word : '{user_word}'")
            user_words.remove(user_word)
            continue

        user_input = get_user_input("Votre réponse", user_word)

        if user_input == 'q':
            break

        elif user_input != 'n' :

            result = find_a_translation(user_word, user_input, translations)
            if len(user_input) > 0 and len(result) == 0 :
                user_words.remove(raw_word)
                print(f"\n[CORRECTE]\n")
            else :
                if len(user_input) == 0 :
                    print(f"\nTraduction possible :\n")
                    print(format_(result))
                else :
                    input(f"\n[INCORRECTE] Traduction possible :\n")
                    print(format_(result))
                    maybe = input("\nIt was correct [y/*] : ")
                    if maybe == 'y' :
                        user_words.remove(user_word)
        else :
            user_words.remove(user_word)

        print("\n-----------------------------------------")

