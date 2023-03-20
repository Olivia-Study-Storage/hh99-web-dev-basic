from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.grjwzgf.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
  return render_template('index.html')

# 등록
@app.route('/bucket', methods=['POST'])
def bucket_post():
  bucket_receive = request.form['bucket_give']
  # 시퀀스 번호 만들기: 전체 길이에 +1
  bucket_list = list(db.bucket.find({}, {'_id': False}))
  bucket_sequence = len(bucket_list) + 1
  doc = {
    'num': bucket_sequence,
    'bucket': bucket_receive,
    'done': 0,
  }
  db.bucket.insert_one(doc)
  return jsonify({'msg': '버킷리스트 등록 완료 👍'})

# 수정 - done
@app.route("/bucket/done", methods=["POST"])
def bucket_done():
  num_receive = request.form['num_give']
  db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
  return jsonify({'msg': '꿈을 하나 이뤘어요 🌠'})

# 수정 - cancel
@app.route("/bucket/cancel", methods=["POST"])
def bucket_cancel():
  num_receive = request.form['num_give']
  db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})
  return jsonify({'msg': '다시 한 번 도전해봐요 💪'})

# 조회
@app.route('/bucket', methods=['GET'])
def bucket_get():
  bucket_list = list(db.bucket.find({}, {'_id': False}))
  return jsonify({'buckets': bucket_list})

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)