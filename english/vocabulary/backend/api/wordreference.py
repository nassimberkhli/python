# ./backend/api/wordreference.py
# Client HTTP vers l'API WordReference déployée (plus de scraping local)

import os
import requests
from .variables import wr_available_dictionaries  # on garde la liste pour la CLI (-l)

API_BASE = os.getenv("WR_API_BASE", "https://api-wordreference-kskt.vercel.app").rstrip("/")


def print_available_dictionaries():
    print('Code  :  Dictionary\n-------------------')
    for code, name in wr_available_dictionaries:
        print(f"{code} : {name}")


def fetch_translation(word: str, dict_code: str, specefic_meanings=None):
    """
    Appelle l'API distante et renvoie (translations_dict, audio_links)
    pour rester compatible avec le code existant (src/revision.py utilise translations[0]).
    On adapte légèrement le format pour que src/revision.py continue de fonctionner :
      - 'word' et 'definition' sont enveloppés dans une liste : ['...']
        (car revision.py accède à translation['word'][0])
    """
    if specefic_meanings is None:
        specefic_meanings = []

    try:
        # Construction propre de la query string (répéter meanings=)
        params = {"word": word, "dict": dict_code}
        for m in specefic_meanings:
            # requests gère la répétition si on passe une liste sous la même clé
            params.setdefault("meanings", []).append(int(m))

        resp = requests.get(f"{API_BASE}/translate", params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        # data attendu :
        # {
        #   "translation": { "1": { "word": "...", "definition": "...", "meanings": [...], "examples": [...] }, ... },
        #   "audio_links": ["https://...mp3", ...]
        # }

        raw_translations = data.get("translation", {}) or {}
        audio_links = data.get("audio_links", []) or []

        # ⚙️ Adapter le shape pour src/revision.py :
        # - word -> [word]
        # - definition -> [definition]
        # - meanings : déjà liste -> ok
        # - examples : laissé tel quel (revision.py ne l'utilise pas)
        adapted = {}
        for k, v in raw_translations.items():
            if not isinstance(v, dict):
                continue
            word_val = v.get("word", "")
            def_val = v.get("definition", "")
            meanings_val = v.get("meanings", []) or []
            examples_val = v.get("examples", []) or []

            adapted[int(k)] = {
                "word": [word_val] if isinstance(word_val, str) else word_val,
                "definition": [def_val] if isinstance(def_val, str) else def_val,
                "meanings": meanings_val,
                "examples": examples_val,
            }

        return adapted, audio_links

    except requests.RequestException as e:
        print(f"[wordreference] HTTP error: {e}")
        return {}, []
    except ValueError:
        print("[wordreference] Failed to decode JSON response")
        return {}, []

