import requests 
from bs4 import BeautifulSoup
import json 
url=input("Введіть URL  веб-сторінки: ")
keywords_input=input("Введіть ключові слова:")

keywords=keywords_input.split()
response=requests.get(url)
html=response.text

soup=BeautifulSoup(html, "html.parser")
text=soup.get_text().lower()
results={}

for word in keywords:
    count=text.count(word.lower())
    results[word]=count

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Результат записано у results.json")
