import re
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

dt = pd.DataFrame(columns=["title", "year", "rating","votes","runtime","genres"])
d={"title":[], "year":[], "rating":[], "votes":[], "runtime":[], "genres":[]}
url = 'https://www.imdb.com/chart/top/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
time.sleep(1)

'''
почему-то в Dev Tools отображалось сразу все 250 фильмов, но как оказалось они подгружались из js во время прокрутку
поэтому нашел список ссылок внутри js и спарсил оттуда
'''
matches = re.findall(r'https://www\.imdb\.com/title/tt\d+/', soup.prettify()) 
for i in matches:
    try:
        response = requests.get(i, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        class_any = soup.find(class_="ipc-inline-list ipc-inline-list--show-dividers sc-103e4e3c-2 cMcwpt baseAlt baseAlt").find_all("li")
        d["runtime"]+=[class_any[-1].text]
        d["year"]+=[class_any[0].text]

        d["title"]+=[soup.find(class_="hero__primary-text").text]
        d["rating"]+=[soup.find(class_="sc-d541859f-1 imUuxf").text]
        d["votes"]+=[soup.find(class_="sc-d541859f-3 dwhNqC").text]
        d["genres"]+=[soup.find(class_="ipc-chip ipc-chip--on-baseAlt").text]
        time.sleep(1)
    except Exception as e:
        print(e)
        d["title"]+=[None]
        d["year"]+=[None]
        d["rating"]+=[None]
        d["votes"]+=[None]
        d["runtime"]+=[None]
        d["genres"]+=[None]

with open("./task_3/top250_raw.csv", "w") as file:
    pd.DataFrame(d).to_csv(file)

#138