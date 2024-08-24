import requests
from bs4 import BeautifulSoup
url="https://jsonplaceholder.typicode.com/posts"
r=requests.get(url)
# print(r.text)
data={
    "userId": 10,
    "id": 99,
    "title": "temporibus sit alias delectus eligendi possimus magni",
    "body": "quo deleniti praesentium dicta non quod\naut est molestias\nmolestias et officia quis nihil\nitaque dolorem quia"
  },
headers={
    'Content-type': 'application/json; charset=UTF-8',
  }

r=requests.post(url, headers=headers, json=data)
print(r.text)

url="https://www.codewithharry.com/blogpost/how-algorithmic-trading-systems-work/"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)

url="https://newsapi.org/"
response=requests.get(url)
print(response.text)
url="https://newsapi.org/v2/everything?q=tesla&from=2024-07-10&sortBy=publishedAt&apiKey=fcdc4567a3f54d00b63f808914cb1273"
response=requests.get(url)
print(response)