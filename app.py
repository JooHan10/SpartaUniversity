from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.zkbjjmk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def classes_post():
    comment_receive = request.form['comment_give']

    doc = {
        'comment':comment_receive
    }
    db.classes.insert_one(doc)

    return jsonify({'msg':'작성 완료!'})

@app.route("/guestbook", methods=["GET"])
def classes_get():
    classes_data = list(db.classes.find({},{'_id':False}))
    return jsonify({'result':classes_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
