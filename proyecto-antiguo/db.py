from flask import Flask
from flask_sqlalchemy import SQLAlchemy  

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./CodigoPython/crawler-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)  

#Se crea base de datos con SQLAlchemy, donde s0 corresponde al valor de un servomoto y s1 el valor del otro servomotor  

# class Epoca(db.Model):
#     __tablename__ = 'epoca'

    
#     id = db.Column(db.Integer, primary_key=True)
#     S0 = db.Column(db.Integer, nullable=False)
#     S1 = db.Column(db.Integer, nullable=False)
#     #encoder = db.Column(db.Integer, nullable=False)
#     matriz = db.Column(db.Integer, nullable=False)
    
    
#     def save(self):
#         if not self.id:
#             db.session.add(self)
#         db.session.commit()
    
#     @staticmethod
#     def get_by_id(id):
#         return User.query.get(id)

#id es el identificador de la tabla y Q es la matriz Q almacenada en formato pickle 

class MatrizQ(db.Model):
    __tablename__ = 'matrizQ'

    id = db.Column(db.Integer, primary_key=True)
    Q = db.Column(db.PickleType, nullable=False)

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    

    
