import requests
from bs4 import BeautifulSoup

def translate(word):
    url = f"https://en.wiktionary.org/api/rest_v1/page/definition/{word}"
    r = requests.get(url, headers={"Accept":"application/json", "User-Agent": "MyWiktionaryParser/1.0 (contact: joshuawoodbridge2022@gmail.com)"}).json()
    
    definitions = []
    
    if "pl" in r:
        for define in r["pl"]:
            soup = BeautifulSoup(define["definitions"][0]["definition"], "html.parser")
            obj = soup.find("a")
            if obj != None:
                definitions.append(obj.get_text())
    
    if definitions != []:
        return definitions[0]
    else:
        print(word + " had no translation")
        return "No translation found"
