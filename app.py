from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ucyg0qc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

#메인페이지
@app.route('/')
def home():
    return render_template('index_real_main.html')

#수강목록페이지
@app.route('/detail')
def detail():
    return render_template('index_detail_1.html')

#소개페이지1
@app.route('/intro1')
def intro1():
    return render_template('index_introduce_kgh.html')

#소개페이지2
@app.route('/intro2')
def intro2():
    return render_template('index-introduce_mdh.html')

#소개페이지3
@app.route('/intro3')
def intro3():
    return render_template('index_introduce_lsm.html')

#소개페이지4
@app.route('/intro4')
def intro4():
    return render_template('index_introduce_ljh.html')

#소개페이지5
@app.route('/intro5')
def intro5():
    return render_template('index_introduce_hsy.html')

#후기 저장하기
@app.route("/comment", methods=["POST"])
def comment_post():
    name_receive = request.form['name_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    #빈칸이 있을 때
    if name_receive == '':
        return jsonify({'msg':'닉네임을 입력해주세요!'})
    if star_receive == '-- 선택하기 --':
        return jsonify({'msg':'별점을 입력해주세요!'})
    if comment_receive == '':
        return jsonify({'msg':'후기를 입력해주세요!'})

    doc = {        
        'name': name_receive,
        'star': star_receive,
        'comment': comment_receive
    }
    db.spartauniversity.insert_one(doc)

    return jsonify({'msg':'후기 저장 완료!'})

#후기 불러오기
@app.route("/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.spartauniversity.find({}, {'_id': False}))
    
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)