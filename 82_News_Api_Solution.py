import requests
import json
query=input("What news do you want to print: ")
num_article= int(input("How manay Title and their Discription do you want to hear or print: "))
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-07-12&sortBy=publishedAt&apiKey=fcdc4567a3f54d00b63f808914cb1273"
r=requests.get(url)
# print(r.text)
news=json.loads(r.text)
for i, article in enumerate(news["articles"]):
    if i>=num_article:
        break
    title=article["title"]
    Description=article["description"]
    print(title)
    print(Description)
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
s=input()
speaker.Speak(f"{title} {Description}")
