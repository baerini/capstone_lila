from flask import Flask, request, make_response, jsonify, render_template, redirect, url_for
from flask_jwt_extended import *
from flask_socketio import SocketIO, emit
from sqlalchemy import asc
from sqlalchemy.exc import NoResultFound
import json
# from flask_sqlalchemy import SQLAlchemy

from config import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

from models import *
from dtos import *

socketio = SocketIO(app)
app.config['JWT_SECRET_KEY'] = "super-secret"
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

jwt = JWTManager(app)

@app.route('/', methods=['GET'])
@jwt_required(optional=True)
def index():
    current_user_id = get_jwt_identity()
    if current_user_id:
        try:
            return render_template('home.html')
        except NoResultFound:
            return render_template('welcome.html')
    else:
        return render_template('welcome.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('information.html')
    elif request.method == 'POST':
        data = request.get_json()
        
        # id, pw, name, gender, age
        user_id = data['id']
        user_pw = data['pw']
        user_name = data['name']
        user_age = data['age']
        user_gender = data['gender']
        
        new_user = User(
            id=user_id,
            pw=user_pw,
            name=user_name,
            age=int(user_age), 
            gender=user_gender,
            success=False
        )
        db.session.add(new_user)
        db.session.commit()
        
        response = make_response()
        return response
    
@app.route('/signup_2/<id>', methods=['GET', 'POST'])
def signup_2(id):
    if request.method == 'GET':
        return render_template('profile.html')
    elif request.method == 'POST':
        user = User.query.filter_by(id=id).first()

        if user and not user.success:
            # job, hobby, fluent, learn, level
            data = request.get_json()

            user.job = data['profession']
            user.hobby = data['hobby']
            user.fluent = data['fluent']
            user.learning = data['learning']
            user.level = data['level']
            user.email = "korea@naver.com" #위치 수정
            user.url = "default.png" #위치 수정
            user.bio = "hello world"
            user.success = True

            db.session.commit()
        
            response = make_response()
            return response
        else:
            return render_template('information.html')

@app.route('/success', methods=['GET'])
def success():
    return render_template('joined.html')

@app.route('/login', methods=['GET', 'POST'])
def login_proc():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        data = request.get_json()
        
        user_id = data['id']
        user_pw = data['pw']
        
        try:
            db.session.query(User).filter(User.id==user_id, User.pw==user_pw).first() 
            access_token = create_access_token(identity=user_id, expires_delta=False)
            response = make_response(redirect('/'))
            set_access_cookies(response, access_token)
            
            return response
        
        except NoResultFound:
            return jsonify(result="Invalid Params") # red screen

@app.route('/users', methods=['GET'])
@jwt_required(optional=True)
def users():
    current_user_id = get_jwt_identity()
    user_dtos = []
    users = User.query.all()
    for user in users:
        if (user.id.decode() == current_user_id) or not user.success:
            continue
        user_dtos.append(user_to_dto(user))
        
    if current_user_id:
        return render_template('users.html', users=user_dtos)
    else:
        return render_template('login.html')

@app.route('/create_chatroom', methods=['POST'])
@jwt_required(optional=True)
def create_chatroom():
    current_user_id = get_jwt_identity()
    data = request.get_json()
        
    username = data['name']
    user1 = User.query.filter_by(id=current_user_id).first()
    user2 = User.query.filter_by(name=username).first() # 수정필요
    
    print(user1, user2)
    chatroom = Chatroom.query.filter(
        (Chatroom.user1_id == user1.id) & (Chatroom.user2_id == user2.id) |
        (Chatroom.user1_id == user2.id) & (Chatroom.user2_id == user1.id)
    ).first()
    
    if chatroom:
        return jsonify({'id': chatroom.chatroom_id})
    else:
        new_chatroom = Chatroom(
            user1_id=user1.id.decode(),
            user2_id=user2.id.decode(),
            state = False
        )
        db.session.add(new_chatroom)
        db.session.commit()
        
        return jsonify({'id': new_chatroom.chatroom_id})

@app.route('/chatrooms', methods=['GET'])
@jwt_required(optional=True)
def chatrooms():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    
    chatrooms = Chatroom.query.filter(
        (Chatroom.user1_id == user.id) | (Chatroom.user2_id == user.id)
    ).order_by(asc(Chatroom.final_time)).all()
    
    chatroom_dtos = []
    for chatroom in chatrooms:
        if chatroom.state:
            receiver = None
            if user.id == chatroom.user1_id:
                receiver = User.query.filter_by(id=chatroom.user2_id).first()
            else:
                receiver = User.query.filter_by(id=chatroom.user1_id).first()
            
            chatroom_dtos.append(
                {
                    "id": chatroom.chatroom_id,
                    "receiver": user_to_dto(receiver),
                    "final_message": chatroom.final_message.decode(),
                    "final_time": chatroom.final_time
                }
            )
            print(chatroom_dtos)
            
    if current_user_id:
        return render_template('chatrooms.html', chatrooms=chatroom_dtos, sender=user_to_dto(user))
    else:
        return render_template('login.html')
    
@app.route('/get_chatrooms', methods=['GET'])
@jwt_required(optional=True)
def get_chatrooms():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    
    chatrooms = Chatroom.query.filter(
        (Chatroom.user1_id == user.id) | (Chatroom.user2_id == user.id)
    ).all()
    
    chatroom_dtos = []
    for chatroom in chatrooms:
        if chatroom.state:
            receiver = None
            if user.id == chatroom.user1_id:
                receiver = User.query.filter_by(id=chatroom.user2_id).first()
            else:
                receiver = User.query.filter_by(id=chatroom.user1_id).first()
            
            receiver = user_to_dto(receiver)
            chatroom_dtos.append(
                {
                    "id": chatroom.chatroom_id,
                    "name": receiver.name, 
                    "url": receiver.url,
                    "final_message": chatroom.final_message.decode(),
                    "final_time": chatroom.final_time
                }
            )

    return chatroom_dtos
    
@app.route('/chatroom/<id>', methods=['GET', 'POST'])
@jwt_required(optional=True)
def chatroom(id):
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    
    ## 나의 채팅목록
    chatrooms = Chatroom.query.filter(
        (Chatroom.user1_id == user.id) | (Chatroom.user2_id == user.id)
    ).all()
    
    chatroom_dtos = []
    for chatroom in chatrooms:
        if chatroom.state:
            receiver = None
            if user.id == chatroom.user1_id:
                receiver = User.query.filter_by(id=chatroom.user2_id).first()
            else:
                receiver = User.query.filter_by(id=chatroom.user1_id).first()
            
            chatroom_dtos.append(
                {
                    "id": chatroom.chatroom_id,
                    "receiver": user_to_dto(receiver),
                    "final_message": chatroom.final_message.decode(),
                    "final_time": chatroom.final_time
                }
            )
            
    ## 선택된 채팅방 메시지 목록
    chatroom = Chatroom.query.filter_by(chatroom_id=id).first()
    
    ## 상대방
    user2 = None
    if chatroom.user1_id == user.id:
        user2 = User.query.filter_by(id=chatroom.user2_id.decode()).first()
    else:
        user2 = User.query.filter_by(id=chatroom.user1_id.decode()).first()
        
    messages = Message.query.filter_by(chatroom_id=id).all()
    receiver = None
    
    message_dtos = []
    for message in messages:
        sender = User.query.filter_by(id=message.sender_id).first()
        receiver = User.query.filter_by(id=message.receiver_id).first()
        message_dtos.append(
                {
                    "sender": user_to_dto(sender),
                    "receiver": user_to_dto(receiver),
                    "message": message.message.decode(),
                    "created_at": message.created_at
                }
            )
        
    return render_template('chatroom.html', id=id, chatrooms=chatroom_dtos, sender=user_to_dto(user), receiver=user_to_dto(user2), messages=message_dtos)

@socketio.on('message')
def handle_message(data):
    d = json.loads(data)
    
    chatroom_id = d.get('id')
    sender_name = d.get('sender')
    receiver_name = d.get('receiver')
    message = d.get('message')
    
    print(d)
    chatroom = Chatroom.query.filter_by(chatroom_id=chatroom_id).first()
    sender = User.query.filter_by(name=sender_name).first()
    receiver = User.query.filter_by(name=receiver_name).first()
    if not chatroom.state:
        chatroom.state = True
    chatroom.final_message = message
    chatroom.final_time = datetime.now()
    
    new_message = Message(
        chatroom_id=chatroom.chatroom_id,
        sender_id=sender.id.decode(),
        receiver_id=receiver.id.decode(),
        message=message,
        created_at=datetime.now(), 
    )
    print(new_message)
    db.session.add(new_message)
    db.session.commit()
    
    emit('message', data, broadcast=True)

@app.route('/profile', methods=['GET', 'POST'])
@jwt_required(optional=True)
def editProfile():
    current_user_id = get_jwt_identity()
    if current_user_id:
        if request.method == 'GET':
            user = User.query.filter_by(id=current_user_id).first()
            userDto = user_to_dto(user)
            return render_template('editProfile.html', user=userDto)
        elif request.method == 'POST':
            user = User.query.filter_by(id=current_user_id).first()

            if user:
                data = request.get_json()

                user.name = data['name']
                user.email = data['email']
                user.gender = data['gender']
                user.age = data['age']
                user.job = data['profession']
                user.hobby = data['hobby']
                user.fluent = data['fluent']
                user.learning = data['learning']
                user.bio = data['bio']

                db.session.commit()
            
                response = make_response()
                return response
            else:
                return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/protected', methods=['GET'])
@jwt_required(optional=True)
def protected():
    current_user_id = get_jwt_identity()
    if current_user_id:
        return jsonify(logged_in_as=current_user_id), 200
    else:
        return jsonify(logged_in_as="anonymous user"), 200
    
@app.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    response = make_response(redirect('/'))
    unset_jwt_cookies(response)
    return response

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # app.run(debug=True)
    socketio.run(app, debug=True, port=5000)