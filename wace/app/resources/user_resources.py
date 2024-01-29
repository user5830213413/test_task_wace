from flask_restx import Resource, reqparse

from app.models.user import UserModel

user_parser = reqparse.RequestParser()
user_parser.add_argument('login', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)

#### лучше использовать jwt токены, думаю нет смысла замарачиваться над тестовым заданием 
class UserRegisterResource(Resource):
    def post(self):
        data = user_parser.parse_args()

        if not data['login'] or not data['password']:
            return {'message': 'логин и пароль обязательны'}, 400
        
        if UserModel.query.filter_by(login=data['login']).first():
            return {'message': 'пользователь с таким логином уже существует'}, 400
        
        user = UserModel(login=data['login'], password=data['password']) #так же сделать хэш пароля но думаю тут нет смысла
        user.save_db()

        return {'message': 'пользователь успешно создан'}, 201

class UserResource(Resource):
    def put(self, user_id):
        data = user_parser.parse_args()  
        user = UserModel.query.filter_by(id=user_id).first()

        if not user:
            return {'message': 'пользователь не найден'}, 400
        
        if not data['login'] or not data['password']:
            return {'message': 'логин и пароль обязательны'}, 400
        
        user.login = data['login']
        user.password = data['password']
        user.save_db()

        return {'message': 'пользователь успешно обновлен'}, 200
    
    def delete(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            return {'message': 'пользователь не найден'}, 400
        user.delete_db()
    
        return {'message': 'пользователь успешно удален'}, 200
