from sqlalchemy import Column, Integer, Double, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from db import Base

"""
user
"""
class User(Base):
    __tablename__ = "User"
    
    user_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
    gender = Column(String(255))
    mbti = Column(String(255))
    job = Column(String(255))
    hobby = Column(String(255))

"""
social
"""
class Friend(Base):
    __tablename__ = "Friend"
    
    friend_id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('User.user_id'))
    to_user_id = Column(Integer, ForeignKey('User.user_id'))
    state = Column(Boolean)
    
class Rating(Base):
    __tablename__ = "Rating"
    
    rating_id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('User.user_id'))
    to_user_id = Column(Integer, ForeignKey('User.user_id'))
    rating = Column(Double)

"""
lang
"""
class Language(Base):
    __tablename__ = "Language"
    
    language_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    
class User_Language(Base):
    __tablename__ = "User_Language"
    
    user_language_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    language_id = Column(Integer, ForeignKey('Language.language_id'))
    level = Column(Integer)

"""
country
"""
class Country(Base):
    __tablename__ = "Country"
    
    country_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    
class User_Country(Base):
    __tablename__ = "User_Country"
    
    user_country_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    country_id = Column(Integer, ForeignKey('Country.country_id'))

"""
chat
"""
class Chatroom(Base):
    __tablename__ = "Chatroom"
    
    chatroom_id = Column(Integer, primary_key=True)
    state = Column(Boolean)
    
class User_Chatroom(Base):
    __tablename__ = "User_Chatroom"
    
    user_chatroom_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    chatroom_id = Column(Integer, ForeignKey('Chatroom.chatroom_id'))

class Message(Base):
    __tablename__ = "Message"
    
    message_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    chatroom_id = Column(Integer, ForeignKey('Chatroom.chatroom_id'))
    message = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
