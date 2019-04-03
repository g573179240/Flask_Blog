#工作
#1.创建Flask应用以及各种配置
#2.创建数据库实例
#3.通过蓝图关联其他的业务程序
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['DEBUG']=True
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/lgc_blog'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    app.config['SECRET_KEY']='luoguichuan'

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    return app