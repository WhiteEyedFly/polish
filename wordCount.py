import json
import xml.sax
import re

wiki_dict = {}
sourceDict = {
    "english": "dictionariesMade/enDict.json",
    "polish": "dictionariesMade/plDict.json"
}

def open_dict(input_file):
    with open(input_file) as f:
        return json.load(f)
    
def wiki_sum(wiki_dict, dictionary):
    for word in dictionary:
        dictionary[word]["count"] = 0
        
        for form in dictionary[word]["forms"]:
            if form["form"] in wiki_dict:
                dictionary[word]["count"] = dictionary[word]["count"] + wiki_dict[form["form"]]
    return dictionary

def find_counts(language, wiki_dict):
    dictionary = open_dict(sourceDict[language])
    dictionary = wiki_sum(wiki_dict, dictionary)
    
    # Fill in blanks
    for item in dictionary:
        if "count" not in dictionary[item]:
            dictionary[item] = 0
    
    # Order based on counts
    sub_dict = {}
    temp_dict = {}
    
    for item in dictionary:
        sub_dict[item] = dictionary[item]["count"]
    sub_dict = {k: v for k, v in sorted(wiki_dict.items(), key=lambda item: item[1], reverse=True)}
    
    for item in sub_dict:
        if item in dictionary:
            temp_dict[item] = dictionary[item]
    
    with open(sourceDict[language], "w") as f:
        json.dump(temp_dict, f, indent=4)
        
def split_list(list):
    empty = []
    for item in range(len(list)):
        empty = empty + item.split()
        
    return empty
    
def clean(text):
    # Remove punctuation
    # Remove numbers
    
    #print(text)
    text = re.sub(r'[^\w\s]', " ", text)
    text = re.sub(r'\d+', " ", text)
    #print(text)
    #print(" ")
    return text

def add_sum(dictionary, text):
    text = text.split()
    for word in text:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

class handler(xml.sax.ContentHandler):
    """
    # https://wiki.python.org/moin/Sax.html
    def startElement(self, name, attrs):
        if name == "title":
            print(attrs.getValue("attribute1"))
            for (k,v) in attrs.items():
                print(k + " " + v)
    """
    # https://stackoverflow.com/questions/15177863/how-can-i-get-and-store-the-text-between-xml-tags-as-a-string-with-the-python-sa
    def __init__(self):
        self.text = []
        self.keeping_text = False
        self.attributes = []

    def startElement(self, name, attrs):
        if name.lower() in ('text'):
            self.keeping_text = True

    def endElement(self, name):
        self.keeping_text = False
        return self.text

    def characters(self, content):
        if self.keeping_text:
            ccon = clean(content)
            #self.text.append(ccon)
            add_sum(wiki_dict, ccon)
   
def strip_rubbish(dictionary, rubbish_min):
    new_dict = {}
    
    for item in dictionary:
        if dictionary[item] > rubbish_min:
            new_dict[item] = dictionary[item]
    
    return new_dict
    
def main(language):
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler())
    parser.parse(open("wikipediasUnparsed/" + language + "Wiki.xml","r"))
    
    # Temp save and recall functions
    """
    with open("wordCounts/" + language + "WordsByCommonality.json", "w") as f:
        json.dump(wiki_dict, f, indent=4)
    with open("wordCounts/" + language + "WordsByCommonality.json", "r") as f:
        wiki_dict = json.load(f)
    """
    
    wiki_dict = strip_rubbish(wiki_dict, 30)
    wiki_dict = {k: v for k, v in sorted(wiki_dict.items(), key=lambda item: item[1], reverse=True)}
        
    find_counts(language, wiki_dict)
    
    with open("wordCounts/" + language + "WordsByCommonality.json", "w") as f:
        json.dump(wiki_dict, f, indent=4)

main("polish")