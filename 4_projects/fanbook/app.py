from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.grjwzgf.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
  return render_template('index.html')

# 등록
@app.route("/fanbook", methods=["POST"])
def guestbook_post():
  nickname_receive = request.form['nickname_give']
  comment_receive = request.form['comment_give']
  doc = {
    'nickname': nickname_receive, 'comment': comment_receive,
  }
  db.fanbook.insert_one(doc)
  return jsonify({'msg': '뉴진스를 향한 응원이 등록되었어요 🐰'})

# 조회
@app.route("/fanbook", methods=["GET"])
def guestbook_get():
  fanbook_list = list(db.fanbook.find({}, {'_id': False}))
  return jsonify({'fanbooks': fanbook_list})

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)