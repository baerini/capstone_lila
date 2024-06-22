from models import *

class UserDto:
    def __init__(self, user_id, name, age, gender, email, job, hobby, fluent, learning, level, url, success, bio):
        self.user_id = user_id
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
        user_id=user.user_id,
        name=user.name,
        age=user.age,
        gender=user.gender,
        email=user.email,
        # mbti=user.mbti,
        job=user.job,
        hobby=user.hobby,
        fluent=user.fluent,
        learning=user.learning,
        level=user.level,
        url=user.url,
        bio=user.bio,
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
#         receiver=receiver,
#         # user2_id=chatroom.user2_id,
#         state=chatroom.state
#     )
