from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

# ! GET 방식
# [methods=['GET']] get 요청으로 들어온다. ['/test'] 어디로? /test라는 창구로!
@app.route('/test', methods=['GET'])
def test_get():
   # 그때 만약 title_give라는 데이터가 있으면 가져와서 title_receive라는 변수에 넣는다.
   title_receive = request.args.get('title_give')
   print(title_receive)
   # 백에서 프론트로 데이터를 내려줄 때 아래와 같이 내려준다.
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

# ! POST 방식
# [methods=['POST']] post 요청으로 들어온다. ['/test'] 어디로? /test라는 창구로!
@app.route('/test', methods=['POST'])
def test_post():
   # 그때 만약 title_give라는 데이터가 있으면 가져와서 title_receive라는 변수에 넣는다.
   title_receive = request.form['title_give']
   print(title_receive)
   # 백에서 프론트로 데이터를 내려줄 때 아래와 같이 내려준다.
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)