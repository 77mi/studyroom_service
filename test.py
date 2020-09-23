from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app, use_native_unicode='utf8')


class User(db.Model):
    #声明表名
    __tablename__ = 'user'
    #建立字段函数
    id = db.Column(db.String(200),primary_key=True)
    name = db.Column(db.String(200))
    password = db.Column(db.String(200))
    email = db.Column(db.String(200))
    birth = db.Column(db.DATE)
    sex = db.Column(db.String(200))
    picture = db.Column(db.String(200))
    rank = db.Column(db.Integer)
    detail = db.Column(db.String(200))
    status = db.Column(db.String(200))
    signdate = db.Column(db.DATE)


class Chat_main(db.Model):
    __tablename__ = 'chat_main'
    id = db.Column(db.String(200),primary_key=True)
    topic = db.Column(db.String(200))
    publishid = db.Column(db.String(200))

@app.route("/select/user")
def select_user():
    data = json.loads(request.get_data())
    print(data)
    ulist = User.query.filter(User.id==data.get("id")).all()
    udict={}
    for item in ulist:
        udict["id"]=item.id
        udict["name"]=item.name
        udict["password"]=item.password
        udict["email"]=item.email
        udict["birth"]=str(item.birth)
        udict["sex"]=item.sex
        udict["picture"]=item.picture
        udict["rank"]=item.rank
        udict["detail"]=item.detail
        udict["status"]=item.status
        udict["signdate"]=str(item.signdate)
    print(udict)
    return json.dumps(udict)


@app.route("/select/user/core")
def select_user_core():
    data = json.loads(request.get_data())
    print(data)
    ulist = User.query.filter(User.id==data.get("id")).all()
    udict={}
    for item in ulist:
        udict["id"]=item.id
        udict["name"]=item.name
        udict["password"]=item.password
    print(udict)
    return json.dumps(udict)

    
@app.route("/select/chat_main")
def select_chat_main():
    data = json.loads(request.get_data())
    print(data)
    ulist = Chat_main.query.filter(Chat_main.topic==data.get("topic") and Chat_main.publishid==data.get("publishid")).all()
    udict={}
    for item in ulist:
        udict["id"]=item.id
        udict["topic"]=item.topic
        udict["publishid"]=item.publishid
    print(udict)
    return json.dumps(udict)


if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run(host='0.0.0.0')