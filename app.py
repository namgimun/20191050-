from flask import Flask, request, render_template, url_for, redirect, abort
app = Flask(__name__)

import game
import json
import dbdb

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html', data=character)

@app.route('/gamestart>')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(character['items'])
    return ("{} 이 {} 아이템을 사용 해서 이겼다.".format(character["name"], character["items"][0]))

@app.route('/input/<int:num>')
def intput_num(num):
    if num == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['items'])
        return ("{} 가 {} 아이템을 사용 해서 이겼다.".format(character["name"], character["items"][0]))
    elif num == 2:
        return "도망갔다"
    elif num == 3:
        return "히바리"
    else:
        return "없어요"

@app.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        passward = request.form['passward']
        print (id,type(id))
        print (passward,type(passward))
        if id =="abc" and passward =='1234': 
            return "안녕하세요~ {} 님".format(id)
        else:
            return "아이디 또는 패스워드를 확인 하세요."

@app.route('/getinfo')
def getinfo():
    # 파일 입력
    ret = dbdb.select_all()
    print(ret[3])
    return render_template('getinfo.html', data=ret)
    #return '번호 : {}, 이름 : {}'.format(ret[0], ret[1])

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form["num"]
        name = request.form["name"]
        print(num, name)
        dbdb.insert_data(num, name)
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/naver')
def naver():
    return redirect("http://www.naver.com/")

@app.route('/kakao')
def daum():
    return redirect("http://www.daum.net/")

@app.route('/urltest')
def url_test():
    return redirect(url_for('daum'))

@app.route('/movenaver/<site>')
def movenaver_site(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))

@app.route('/img')
def image():
    return render_template("image.html")


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=True)