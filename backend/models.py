from flask_sqlalchemy import SQLAlchemy
from __main__ import app
from datetime import datetime

db = SQLAlchemy(app)

"""
user
"""
class User(db.Model):
    __tablename__ = "User"
    
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    id = db.Column(db.String(255))
    pw = db.Column(db.String(255))
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(255))
    email = db.Column(db.String(255))
    # mbti = db.Column(db.String(255))
    job = db.Column(db.String(255))
    hobby = db.Column(db.String(255))
    fluent = db.Column(db.String(255))
    learning = db.Column(db.String(255))
    level = db.Column(db.Integer)
    url = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    success = db.Column(db.Boolean)

# class Friend(db.Model):
#     __tablename__ = "Friend"
    
#     friend_id = db.Column('friend_id', db.Integer, primary_key=True)
#     from_user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
#     to_user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
#     state = db.Column(db.Boolean)
    
class Rating(db.Model):
    __tablename__ = "Rating"
    
    rating_id = db.Column('rating_id', db.Integer, primary_key=True)
    from_user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    to_user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    rating = db.Column(db.Integer)

"""
lang
"""
# class Language(db.Model):
#     __tablename__ = "Language"
    
#     language_id = db.Column('language_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
    
# class User_Language(db.Model):
#     __tablename__ = "User_Language"
    
#     user_language_id = db.Column('user_language_id', db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
#     language_id = db.Column(db.Integer, db.ForeignKey('Language.language_id'))
#     level = db.Column(db.Integer)

"""
country
"""
# class Country(db.Model):
#     __tablename__ = "Country"
    
#     country_id = db.Column('country_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
    
# class User_Country(db.Model):
#     __tablename__ = "User_Country"
    
#     user_country_id = db.Column('user_country_id', db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
#     country_id = db.Column(db.Integer, db.ForeignKey('Country.country_id'))

"""
chat
"""
class Chatroom(db.Model):
    __tablename__ = "Chatroom"
    
    chatroom_id = db.Column('chatroom_id', db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    user2_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    final_message = db.Column(db.String(255))
    final_time = db.Column(db.DateTime, default=datetime.now())
    state = db.Column(db.Boolean) # 선톡 전 => 프로필까지만 False, 왼쪽엔 아직

# class User_Chatroom(db.Model):
#     __tablename__ = "User_Chatroom"
    
#     user_chatroom_id = db.Column('user_chatroom_id', db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
#     chatroom_id = db.Column(db.Integer, db.ForeignKey('Chatroom.chatroom_id'))

class Message(db.Model):
    __tablename__ = "Message"
    
    message_id = db.Column('message_id', db.Integer, primary_key=True)
    chatroom_id = db.Column(db.Integer, db.ForeignKey('Chatroom.chatroom_id'))
    sender_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    message = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now())

