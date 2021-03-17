from flask import Flask  #載入Flask物件，建立application
from flask import request #載入request物件，取得要求字串
from flask import render_template #載入render_template樣板檔案
from flask import redirect #載入redirect函式
from flask import session #載入session物件
#建立application 物件
app=Flask(__name__)

#session產生金鑰
#comand: python -c 'import os; print(os.urandom(16))'
app.secret_key='secret'

# homepage路由
@app.route("/")
def homepage():
    return render_template("homepage.html")

#signin驗證的路由
@app.route("/signin", methods=["POST","GET"])
def signin():
    account=request.form["count"]
    password=request.form["password"]
    if account==password=="test":
        session['status']='login' #session記錄使用者為登入狀態
        return redirect("/member")
    else:
        return redirect("/error")


#member成功的路由
@app.route("/member", methods=["POST","GET"])
def member():
    login=session.get('status')  
    if login: #session為登入狀態，導向登入成功頁面
        return render_template("member.html")
    return redirect("/")#session無紀錄登入狀態，導向登入首頁

#error失敗的路由
@app.route("/error")
def error():
    return render_template("error.html")

#signout登出系統的路由
@app.route("/signout")
def signout():
    session.pop('status', None) #刪除使用者登入的狀態
    return redirect("/") 


#執行app，設定網址的埠號
app.run(port=3000)

