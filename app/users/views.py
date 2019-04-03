from . import users
from flask import render_template, session, request, redirect
from ..models import *
@users.route('/users')
def users_views():
    return "这是user访问路径"

@users.route('/login',methods=['GET','POST'])
def login_views():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        #接收前端传递过来的数据
        loginname = request.form.get('username')
        upwd = request.form.get('password')
        #到数据库中去验证数据
        user = User.query.filter_by(loginname=loginname,upwd=upwd).first()
        if user:
            session['uid']=user.id
            session['uname']=user.uname
            return redirect('/')
        else:
            errMsg = "用户名或密码错误"
            return render_template('login.html',errMsg=errMsg)

@users.route('/logout')
def logout_views():
    #获取源地址,有源地址则返回,没有的话则跳转到首页
    url = request.headers.get('referer','/')
    print('源地址'+url)

    #判断登录信息是否在session中
    if 'uid' in session and 'uname' in session:
        del session['uid']
        del session['uname']
    return redirect(url)

@users.route('/register')
def register_views():
    return render_template('register.html')