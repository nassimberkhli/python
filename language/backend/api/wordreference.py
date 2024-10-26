import argparse
import requests
from bs4 import BeautifulSoup

from .variables import URL, wr_available_dictionaries

def print_available_dictionaries() :
    print('Code  :  Dictionary\n-------------------')
    for code, name in wr_available_dictionaries:
        print(f"{code} : {name}")

def fetch_translation(word, dict_code):
    """Fetches and parses translation for a given word and dictionary code."""
    html_content = fetch_page(word, dict_code)
    if html_content:
        return parse_translation(html_content)
    else:
        return {}, []  # Return empty structures if fetching fails


def fetch_page(word, dict_code) :
    """ Fetches the page data from WordReference based on word and dictionary code. """
    try:
        response = requests.get(f"{URL}/{dict_code}/{word}")
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def remove_pos_tags(soup_element):
    """ Removes all 'em' tags with class 'POS2' from a soup element. """
    for pos_tag in soup_element.find_all('em', class_='POS2'):
        pos_tag.decompose()

def update_translation(row, translation):
    """ Updates the translation dictionary with meanings or examples based on row type. """
    if row.find(class_="ToWrd"):
        meaning_elements = row.find_all('td')
        if meaning_elements and len(meaning_elements) > 2:
            meaning_text = meaning_elements[2].get_text().strip()
            translation["meanings"].append(clean_text(meaning_text))
    elif row.find(class_="FrEx") or row.find(class_="ToEx"):
        example_text = row.find('td', class_='ToEx').get_text().strip() if row.find(class_="ToEx") else row.find('td', class_='FrEx').get_text().strip()
        translation["examples"].append(clean_text(example_text))

def parse_translation(html_content) :
    """ Parses the HTML content to extract translations and audio links, ignoring POS2 class elements. """
    soup = BeautifulSoup(html_content, "html.parser")
    results = soup.find_all("tr", {'class': ['even', 'odd']})
    translations = {}
    translation_number = 0
    translation = {}

    for row in results:
        if "more" in row.get('class', []):
            continue

        if row.find(class_="FrWrd") :
            remove_pos_tags(row)
            if translation_number > 0 :
                translations[translation_number] = translation
            translation_number += 1
            translation = extract_translation(row)

        elif row.find(class_="ToWrd") or row.find(class_="FrEx") or row.find(class_="ToEx") :
            update_translation(row, translation)

    if translation_number > 0 :
        translations[translation_number] = translation

    audio_links = extract_audio_links(soup)
    return translations, audio_links

def extract_translation(row) :
    """ Extracts main word and its definitions from a row. """
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
    """ Extracts audio links from the page if available. """
    try:
        script = soup.find("div", id="listen_widget").script.string
        audio_urls = script[18:-3].split(',')
        return [URL + link.strip()[1:-1] for link in audio_urls]
    except:
        return []

def clean_text(text):
    """ Cleans the text extracted from HTML. """
    return text.replace('⇒', '').replace(u'\xa0', u' ').replace(u'\u24d8', u'')
