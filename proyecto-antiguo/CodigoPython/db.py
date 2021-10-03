from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/santiago/Desktop/crawlerbot-master/basededatos.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./crawler-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Epoca(db.Model):
    __tablename__ = 'epoca'

    
    id = db.Column(db.Integer, primary_key=True)
    S0 = db.Column(db.Integer, nullable=False)
    S1 = db.Column(db.Integer, nullable=False)
    #encoder = db.Column(db.Integer, nullable=False)
    matriz = db.Column(db.Integer, nullable=False)
    
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

class MatrizQ(db.Model):
    __tablename__ = 'matrizQ'

    id = db.Column(db.Integer, primary_key=True)
    Q = db.Column(db.PickleType, nullable=False)

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    

    
