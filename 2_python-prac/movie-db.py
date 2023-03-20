from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.grjwzgf.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# '포레스트 검프'의 평점을 가져오기
star = db.movies.find_one({'name':'포레스트 검프'})['star']
print(star)

# '포레스트 검프'의 평점과 같은 평점의 영화 제목들을 가져오기
same_stars = list(db.movies.find({'star':star},{'_id':False}))
for movie in same_stars:
    name = movie['name']
    print(name)

# '쇼생크 탈출'의 평점을 9.2로 만들기
db.movies.update_one({'name':'쇼생크 탈출'},{'$set':{'star':9.2}})