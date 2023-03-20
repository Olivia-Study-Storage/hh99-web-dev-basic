from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.grjwzgf.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/movie", methods=["POST"])
def movie_post():
  url_receive = request.form['url_give']
  star_receive = request.form['star_give']
  comment_receive = request.form['comment_give']

  # url을 기반으로 크롤링하여 나머지 데이터도 같이 insert 한다.
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get(url_receive, headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')
  og_image = soup.select_one('meta[property="og:image"]')['content']
  og_title = soup.select_one('meta[property="og:title"]')['content']
  og_description = soup.select_one('meta[property="og:description"]')['content']

  # url은 데이터 크롤링 시에 필요하지만 db에 저장할 필요는 없으므로, doc에서 제외한다.
  doc = {
    'title':og_title, 'desc':og_description, 'image':og_image,
    'star':star_receive, 'comment':comment_receive, 
  }
  db.movies.insert_one(doc)
  return jsonify({'msg':'등록이 완료되었습니다!'})

@app.route("/movie", methods=["GET"])
def mars_get():
  movie_data = list(db.movies.find({},{'_id':False}))
  return jsonify({'result':movie_data})

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)