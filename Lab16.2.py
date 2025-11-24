import requests
import json
quotes=[]

n=int(input("Скільки цитат отримати?: "))
for i in range(n):
    url="http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
    response=requests.get(url)
    
    data=response.json()
    quote=data["quoteText"]
    author=data["quoteAuthor"]
    
    quotes.append({
        "quote": quote,
        "author": author
    })

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=4)

print("Цитати записано у quotes.json")