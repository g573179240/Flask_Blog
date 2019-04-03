import datetime
import os

from flask import render_template, session, request, redirect
#导入蓝图，用于构筑
from . import main
from ..models import *

@main.route('/')
def index_views():
    categories = Category.query.all()
    topics = Topic.query.all()
    if 'uid' in session and 'uname' in session:
        user = User.query.filter_by(id=session.get('uid')).first()
    return render_template('index.html',params=locals())


@main.route('/release',methods=['GET','POST'])
def release_views():
    #允许发表，实现作者的权限认证
    if request.method == 'GET':
        if 'uid' in session and 'uname' in session:
            user = User.query.filter_by(id=session.get('uid')).first()
            if user.is_author != 1:
                return redirect('/')
            else:
                categories = Category.query.all()
                return render_template('release.html',params=locals())
        else:
            return redirect('/login')
    #将发表的博客保存进数据库
    else:
        topic = Topic()
        topic.title = request.form.get('author')
        topic.category_id = request.form.get('category')
        topic.user_id = session.get('uid')
        topic.content = request.form.get('content')
        topic.pub_date = datetime.datetime.now().strftime("%Y-%m-%d")
        #如果有上传文件
        if request.files:
            f = request.files['picture']
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            ext=f.filename.split('.')[1]
            filename=ftime+"."+ext
            topic.images = "upload/"+filename
            #将文件保存到服务器
            basedir = os.path.dirname(os.path.dirname(__file__))
            upload_path = os.path.join(basedir,'static/upload',filename)
            print(upload_path)
            f.save(upload_path)
        db.session.add(topic)
        return redirect('/')

@main.route('/list')
def list_views():
    categories = Category.query.all()
    topics = Topic.query.all()
    return render_template('list.html',params=locals())

@main.route('/info/<id>',methods=['GET'])
def info_views(id):
    topic = Topic.query.filter_by(id=id).first()
    user = User.query.filter_by(id=session.get('uid')).first()
    return render_template('info.html',params=locals())



@main.route('/about')
def about_views():
    topics = Topic.query.all()
    return render_template('about.html',params=locals())

@main.route('/time')
def time_views():
    topics = Topic.query.all()
    return render_template('time.html',params=locals())

@main.route('/photo')
def photo_views():
    topics= Topic.query.all()
    return render_template('photo.html',params=locals())