from flask import Flask
from flask_restx import Api

from app.models.db import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db.init_app(app)


with app.app_context():
    db.create_all()


from app.resources.user_resources import UserResource, UserRegisterResource
from app.resources.wallet_resources import WalletResource, WalletTransferResource


api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(UserRegisterResource, '/user/register')
api.add_resource(WalletResource, '/wallet/<int:user_id>', '/wallet')
api.add_resource(WalletTransferResource, '/wallet/transfer')