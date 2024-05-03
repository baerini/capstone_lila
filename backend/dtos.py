from models import *

class UserDto:
    def __init__(self, name, age, gender, email, job, hobby, fluent, learning, level, url, success, bio):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        # self.mbti = mbti
        self.job = job
        self.hobby = hobby
        self.fluent = fluent
        self.learning = learning
        self.level = level
        self.url = url
        self.bio = bio
        self.success = success
        
def user_to_dto(user: User):
    return UserDto (
        name=user.name.decode(),
        age=user.age,
        gender=user.gender.decode(),
        email=user.email.decode(),
        # mbti=user.mbti.decode(),
        job=user.job.decode(),
        hobby=user.hobby.decode(),
        fluent=user.fluent.decode(),
        learning=user.learning.decode(),
        level=user.level,
        url=user.url.decode(),
        bio=user.bio.decode(),
        success=user.success
    )
    
# class ChatroomDto:
#     def __init__(self, receiver, state):
#         self.receiver = receiver,
#         # self.user2_id = user2_id
#         self.state = state
        
# def chatroom_to_dto(user: User, chatroom: Chatroom):
#     receiver = None
#     if user.id == chatroom.user1_id:
#         receiver = chatroom.user2_id
#     else:
#         receiver = chatroom.user1_id
        
#     return ChatroomDto (
#         receiver=receiver.decode(),
#         # user2_id=chatroom.user2_id.decode(),
#         state=chatroom.state
#     )