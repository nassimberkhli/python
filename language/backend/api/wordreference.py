import argparse
import re
import requests

from bs4 import BeautifulSoup
from .variables import URL, wr_available_dictionaries

def print_available_dictionaries() :
    print('Code  :  Dictionary\n-------------------')
    for code, name in wr_available_dictionaries:
        print(f"{code} : {name}")

def fetch_translation(word, dict_code, specefic_meanings = []) :
    html_content = fetch_page(word, dict_code)
    if html_content :
        return parse_translation(html_content, specefic_meanings)
    else:
        return {}, []  # Return empty structures if fetching fails


def fetch_page(word, dict_code) :
    try:
        response = requests.get(f"{URL}/{dict_code}/{word}")
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def remove_pos_tags(soup_element) :
    for pos_tag in soup_element.find_all('em', class_='POS2'):
        pos_tag.decompose()

def update_translation(row, translation) :

    if row.find(class_="ToWrd") :
        meaning_elements = row.find_all('td')

        if meaning_elements and len(meaning_elements) > 2 :
            meaning_text = meaning_elements[2].get_text().strip()
            translation["meanings"].append(clean_text(meaning_text, "meanings"))

    elif row.find(class_="FrEx") or row.find(class_="ToEx") :
        if row.find(class_="ToEx") :
            example_text = row.find('td', class_='ToEx').get_text().strip()
        else :
            example_text = row.find('td', class_='FrEx').get_text().strip()
        translation["examples"].append(clean_text(example_text))

def parse_translation(html_content, specific_meanings) :
    soup = BeautifulSoup(html_content, "html.parser")
    results = soup.find_all("tr", {'class': ['even', 'odd']})
    translations = {}
    translation_number = 0
    translation = None

    for row in results :
        if "more" in row.get('class', [1]) :
            continue

        if row.find(class_="FrWrd") :

            remove_pos_tags(row)
            translation = extract_translation(row)
            translation_number += 1

            if translation and (specific_meanings == [] or translation_number in specific_meanings) :
                    translations[translation_number] = translation

        elif row.find(class_="ToWrd") or row.find(class_="FrEx") or row.find(class_="ToEx") :
            if translation and (specific_meanings == [] or translation_number in specific_meanings) :
                update_translation(row, translation)

    if translation and (specific_meanings == [] or translation_number in specific_meanings) :
        translations[translation_number] = translation

    audio_links = extract_audio_links(soup)
    return translations, audio_links

def extract_translation(row) :
    cells = row.find_all('td')
    if len(cells) > 2:
        word_text = cells[0].get_text().strip()
        definition_text = cells[1].get_text().strip()
        meanings_text = cells[2].get_text().strip()
        return {
            "word": clean_text(word_text),
            "definition": clean_text(definition_text),
            "meanings": [clean_text(meanings_text)],
            "examples": []
        }
    return {"word": "", "definition": "", "meanings": [], "examples": []}

def extract_audio_links(soup):
    try:
        script = soup.find("div", id="listen_widget").script.string
        audio_urls = script[18:-3].split(',')
        return [URL + link.strip()[1:-1] for link in audio_urls]
    except:
        return []

def clean_text(text, type_ = "") :
    if type_ == "meanings" :
        text = re.sub(r'[\s,]+\b[a-z]{1,4}\d*\b', '', text, flags=re.IGNORECASE).strip()
    return text.replace('⇒', '').replace(u'\xa0', u' ').replace(u'\u24d8', u'')
