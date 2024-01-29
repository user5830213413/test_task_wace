from .db import db

class WalletModel(db.Model):
    __tablename__ = 'wallet'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    net = db.Column(db.String(55), nullable=False)
    value = db.Column(db.Float(), default=0) # для точности лучше использовать decimal
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    @classmethod
    def get_all_wallets(cls, _id):
        return cls.query.filter_by(user_id=_id).all()
    

    def save_db(self):
        db.session.add(self)
        db.session.commit()