from flask_restx import Resource, reqparse
from sqlalchemy import and_

from app.models.user import UserModel
from app.models.wallet import WalletModel


wallet_parser = reqparse.RequestParser()
wallet_parser.add_argument('login', type=str)
wallet_parser.add_argument('address', type=str)
wallet_parser.add_argument('net', type=str)
wallet_parser.add_argument('summ', type=float)
wallet_parser.add_argument('operation', type=str)

wallet_parser.add_argument('from_address', type=str)
wallet_parser.add_argument('to_address', type=str)


class WalletResource(Resource):
    def get(self, user_id):
        return {'wallets': [{'address': wallet.address, 'net': wallet.net, 'value': wallet.value} for wallet in WalletModel.get_all_wallets(user_id)]}
    
    def post(self):
        data = wallet_parser.parse_args()
        
        if not data['address'] or not data['net'] or not data['login']:
            return {'message': 'адрес, сеть и логин обязательны'}, 400
        
        user = UserModel.query.filter_by(login=data['login']).first()
        if not user:
            return {'message': 'пользователь не найден'}, 404

        wallet = WalletModel(user_id=user.id, address=data['address'], net=data['net'])
        wallet.save_db()

        return {'message': 'кошелек успешно создан'}, 201
    
    def put(self):
        data = wallet_parser.parse_args()

        if not data['address'] or not data['login']:
            return {'message': 'адрес и логин обязательны'}, 400
        
        user = UserModel.query.filter_by(login=data['login']).first()
        if not user:
            return {'message': 'пользователь не найден'}, 404
        
        wallet = WalletModel.query.filter(and_(WalletModel.address == data['address'], WalletModel.user_id == user.id)).first()

        if not wallet:
            return {'message': 'кошелек не найден'}, 404
        
        if data['operation'] == 'addition':
            wallet.value += data['summ']
        elif data['operation'] == 'subtraction':
            wallet.value -= data['summ']
        else:
            return {'message': 'некорректная операция'}, 400
        wallet.save_db()

        return {'message': 'кошелек успешно обновлен'}, 200


class WalletTransferResource(Resource):
    def post(self):
        data = wallet_parser.parse_args()

        user = UserModel.query.filter_by(login=data['login']).first()
        if not user:
            return {'message': 'пользователь не найден'}, 404
        
        from_address = WalletModel.query.filter(and_(WalletModel.address == data['from_address'], WalletModel.user_id == user.id)).first()
        to_address = WalletModel.query.filter_by(address=data['to_address']).first()

        if not from_address:
            return {'message': 'кошелек отправителя не найден'}, 404
        
        if not to_address:
            return {'message': 'кошелек получателя не найден'}, 404

        if from_address.value < data['summ']:
            return {'message': 'недостаточно средств'}, 400
        
        from_address.value -= data['summ']
        to_address.value += data['summ']
        from_address.save_db()
        to_address.save_db()

        return {'message': 'средства успешно переведены'}, 200
