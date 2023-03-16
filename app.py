from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.rqf7gte.mongodb.net/?retryWrites=true&w=majority')
# mongodb+srv://test:sparta@cluster0.ucyg0qc.mongodb.net/?retryWrites=true&w=majority
db = client.SpartaUniversity


#메인페이지
@app.route('/')
def home():
    return render_template('index_main.html')


#수강목록페이지
@app.route('/detail')
def detail():
    teamlist = db.team.find_one({'name': '팀원'}, {'_id': False})
    print(teamlist)
    return render_template('index_detail.html')


#팀원 정보 받기
@app.route("/teamSU", methods=["GET"])
def teamlist_get():
    teamlist = list(db.team.find({}, {'_id': False}))
    return jsonify({'team': teamlist})


#근혜님 소개페이지
@app.route("/1/<id>", methods=["GET"])
def detail_kgh_get(id):
    teamlist = db.team.find_one({'name': id}, {'_id': False})
    reviews = list(db.reviewlist.find({'name':id},{'_id':False}))
    print(teamlist, reviews)
    return render_template('index_introduce_kgh.html', data=teamlist, data1 = reviews)


#동휘님 소개페이지
@app.route("/2/<id>", methods=["GET"])
def detail_mdh_get(id):
    teamlist = db.team.find_one({'name': id}, {'_id': False})
    reviews = list(db.reviewlist.find({'name':id},{'_id':False}))
    print(teamlist, reviews)
    return render_template('index_introduce_mdh.html', data=teamlist, data1 = reviews)


#승민님 소개페이지
@app.route("/3/<id>", methods=["GET"])
def detail_lsm_get(id):
    teamlist = db.team.find_one({'name': id}, {'_id': False})
    reviews = list(db.reviewlist.find({'name':id},{'_id':False}))
    print(teamlist, reviews)
    return render_template('index_introduce_lsm.html', data=teamlist, data1 = reviews)


#주한님 소개페이지
@app.route("/4/<id>", methods=["GET"])
def detail_ijh_get(id):
    teamlist = db.team.find_one({'name': id}, {'_id': False})
    reviews = list(db.reviewlist.find({'name':id},{'_id':False}))
    print(teamlist, reviews)
    return render_template('index_introduce_ijh.html', data=teamlist, data1 = reviews)


#서연님 소개페이지
@app.route("/5/<id>", methods=["GET"])
def detail_hsy_get(id):
    teamlist = db.team.find_one({'name': id}, {'_id': False})
    reviews = list(db.reviewlist.find({'name':id},{'_id':False}))
    print(teamlist, reviews)
    return render_template('index_introduce_hsy.html', data=teamlist, data1 = reviews)


#후기 남기기
@app.route("/saveReview", methods=["POST"])
def reviewlist_add():
    userID_receive = request.form['userID_give']
    Txt_review_receive = request.form['Txt_review_give']
    StarPoint_review_receive = request.form['StarPoint_review_give']
    name_receive = request.form['name_give']

    doc = {
        'userID': userID_receive,
        'Txt_review': Txt_review_receive,
        'StarPoint_review': StarPoint_review_receive,
        'name': name_receive
    }
    db.reviewlist.insert_one(doc)

    return jsonify({'msg': '저장완료!'})


# #댓글 삭제
# @app.route("/del_review", method=["POST"])
# def reviewlist_del():
#     db.reviewlist.delete_one({'name':id})

#     return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)