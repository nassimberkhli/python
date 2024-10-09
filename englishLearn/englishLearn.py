import random
import textwrap

phrases = {}

def quiz() :
    remaining_phrases = list(phrases.keys())
    continu = '\n'

    while remaining_phrases and continu != "stop":
        
        phrase_fr = random.choice(remaining_phrases)
        
        print(f"Traduisez cette phrase:\n\n{textwrap.fill(phrase_fr, width=40)}")
        user_input = input("\n\nVotre réponse (relancer ','): ")
        
        while len(user_input) > 0 and user_input[-1] == ',' :
            print(f"Traduisez cette phrase:\n\n{textwrap.fill(phrase_fr, width=40)}")
            user_input = input("\n\nVotre réponse (relancer ',') : ")
            
        if len(user_input) > 1:
            if user_input[-1] != '.' :
                user_input += '.'
        
        if user_input.strip().lower() == phrases[phrase_fr].strip().lower():
            print("\n[TRUE]")
            remaining_phrases.remove(phrase_fr)
        else:
            print(f"\n[FALSE] :\n\n{textwrap.fill(phrases[phrase_fr], width=40)}")
            continu = input("\nvotre réponse était correcte ? y/n|*/stop ")
            if continu == 'y' :
                remaining_phrases.remove(phrase_fr)
                
        print("\n----------------");
        
    if len(remaining_phrases) == 0 :
        print("[CONGRATULATION] !!!")
            
quiz()