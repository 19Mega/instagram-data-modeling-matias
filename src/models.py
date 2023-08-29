import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Association(Base):
    __tablename__ = 'association'
    follower_id = Column(Integer, ForeignKey('follower.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))
    # relaciones
    followers = relationship('Follower', secondary=Association, lazy='subquery', backref=backref('users', lazy=True))
    posts = relationship('Post', backref='user', lazy=True)
    storys = relationship('Story', backref='user', lazy=True)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    post_date = Column(String(250)) # seria date
    image = Column(String(250)) # seria src
    # relaciones
    medias = relationship('Media', backref = 'post')
    comments = relationship('Comment', backref = 'post')
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    post_date = Column(String(250)) # seria date
    image = Column(String(250)) # seria src
    # relaciones
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    # relaciones
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    author = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    # relaciones
    post_id = Column(Integer, ForeignKey('post.id'))
    author_id = Column(Integer, ForeignKey('user.id'))


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(250))
#     last_name = Column(String(250))
#     email = Column(String(250))
#     password = Column(String(250))

# class Follower(Base):
#     __tablename__ = 'follower'
#     id = Column(Integer, primary_key=True)
#    user_id = Column(Integer, ForeignKey('user.id'))

# class Post(Base):
#     __tablename__ = 'post'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     title = Column(String(250))
#     post_date = Column(String(250)) # seria date
#     image = Column(String(250)) # seria src

# class Story(Base):
#     __tablename__ = 'story'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     title = Column(String(250))
#     post_date = Column(String(250)) # seria date
#     image = Column(String(250)) # seria src

# class Like(Base):
#     __tablename__ = 'like'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user_id = Column(Integer, ForeignKey('story.id'))
#     user_id = Column(Integer, ForeignKey('post.id'))



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
