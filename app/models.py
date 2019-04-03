from . import db

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer,primary_key=True)
    cate_name = db.Column(db.String(50),nullable=False)
    superior = db.Column(db.String(50),nullable=False)
    #和Topic之间的关联关系和反向引用
    topics = db.relationship('Topic',backref='category',lazy='dynamic')

    def __repr__(self):
        return "<Category:%r>"%self.cate_name

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    loginname = db.Column(db.String(50),nullable=False)
    uname = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    url = db.Column(db.String(200))
    upwd = db.Column(db.String(30))
    is_author = db.Column(db.SmallInteger,default=0)
    #增加和topic之间的反向引用
    topics = db.relationship('Topic',backref='user',lazy='dynamic')
    #增加和reply之间的反向引用
    replies = db.relationship('Reply',backref='user',lazy='dynamic')
    #增加和message之间的反向引用
    messages = db.relationship('Message',backref='user',lazy='dynamic')
    #增加与topic之间的反向引用(多对多)
    third1_topics = db.relationship(
        'Topic',
        secondary='third1',
        lazy='dynamic',
        backref=db.backref('third1_user',lazy='dynamic')
    )

class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    pub_date = db.Column(db.DateTime,nullable=False)
    read_num = db.Column(db.Integer,default=0)
    content = db.Column(db.Text,nullable=False)
    images = db.Column(db.Text)
    # 一category对多topic
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    # 一user对多topic
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class Reply(db.Model):
    __tablename__='reply'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text,nullable=False)
    reply_time = db.Column(db.DateTime)
    # 一topic对多reply
    topic_id = db.Column(db.Integer,db.ForeignKey('topic.id'))
    #一user对多reply
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class Message(db.Model):
    __tablename__='message'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text, nullable=False)
    reply_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


#多对多，第三张表
Third1 = db.Table(
    'third1',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('topic_id',db.Integer,db.ForeignKey('topic.id'))
)