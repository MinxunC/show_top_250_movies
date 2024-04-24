import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"}
content = requests.get("https://m.imdb.com/chart/top/", headers=headers).text

soup = BeautifulSoup(content, "html.parser")
all_250_names = soup.find_all("h3", attrs={"class": "ipc-title__text"})
details = soup.find_all("div", attrs={"class": ["sc-b189961a-7", "feoqjK", "cli-title-metadata"]})

for index in range(0, 250):
    print(f"{all_250_names[index+1].string} ------ {details[index].find('span').string}")

