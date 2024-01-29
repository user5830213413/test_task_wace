from .db import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    wallet_id = db.relationship('WalletModel', backref='user', lazy=True)

    def save_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_db(self):
        db.session.delete(self)
        db.session.commit()