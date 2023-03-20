from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.grjwzgf.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#main > div > span > div > div > div.lister > table > tbody > tr')
for tr in trs:
    name = tr.select_one('td.titleColumn > a').text
    year = tr.select_one('td.titleColumn > span').text[1:5]
    star = tr.select_one('td.ratingColumn.imdbRating > strong').text
    # db에 저장하기 위해 딕셔너리 형태로 만들기
    doc = {
        'name': name,
        'year': year,
        'star': star,
    }
    db.movies.insert_one(doc)