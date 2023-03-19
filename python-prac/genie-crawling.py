import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for tr in trs:
    # 순위인 앞에서 2글자만 나올 수 있도록 하고, 공백 줄이 출력되어 strip으로 공백을 없앤다.
    rank = tr.select_one('td.number').text[0:2].strip()
    # 제목 앞 19금이 붙은 곡이 있어 replace로 해당 문자를 제거하고, 공백들을 제거한다.
    title = tr.select_one('td.info > a.title.ellipsis').text.replace('19금', '').strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, artist)