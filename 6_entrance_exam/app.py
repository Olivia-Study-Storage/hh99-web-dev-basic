from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import json
with open("config.json", "r", encoding="utf-8") as f:
  config = json.load(f)

from pymongo import MongoClient
client = MongoClient(config["dbUrl"])
db = client.dbsparta

# index.html
@app.route('/')
def home():
  return render_template('index.html')

# 조회
@app.route('/bucket', methods=['GET'])
def bucket_get():
  bucket_list = list(db.bucket.find({}, {'_id': False}))
  return jsonify({'buckets': bucket_list})

# 저장
@app.route("/bucket", methods=["POST"])
def bucket_post():
  bucket_receive = request.form['bucket_give']
  bucket_list = list(db.bucket.find({}, {'_id': False}))
  count = len(bucket_list) + 1
  doc = {
    'num': count,
    'bucket': bucket_receive,
    'done': 0,
  }
  db.bucket.insert_one(doc)
  return jsonify({'msg': '저장 완료!'})

# 수정
@app.route("/bucket/done", methods=["POST"])
def bucket_done():
  num_receive = request.form['num_give']
  db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
  return jsonify({'msg': '꿈을 하나 이뤘어요 🌠'})

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)