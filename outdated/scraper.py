from bs4 import BeautifulSoup
import requests

words = [line for line in open("wordList.txt", "r")]

for word in range(len(words)):
    words[word] = words[word][:len(words[word])-1]
    
for word in words:
    link = "https://en.bab.la/dictionary/polish-english/" + word
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    translation = soup.findAll("a", attrs={"class":"scroll-link"})
    
    print(soup)
    print(word, translation)