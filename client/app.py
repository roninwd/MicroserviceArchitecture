import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

config = {
    'DATABASE_URI': os.environ.get('DATABASE_URI', ''),
}

app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE_URI']
db = SQLAlchemy(app)
engine = create_engine(config['DATABASE_URI'], echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    age = db.Column(db.Integer)

    @property
    def serialize(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'age': self.age}


@app.route('/clients', methods=['GET'])
def show_list():
    return jsonify([item.serialize for item in Client.query.all()])


@app.route('/clients/<int:id>', methods=['GET'])
def show_one(id):
    return jsonify(Client.query.get(id).serialize)


@app.route('/clients', methods=['POST'])
def create_client():
    request_data = request.get_json()
    name = 'Guest'
    email = 'guest@arch.homework'
    age = 18
    if 'name' in request_data:
        name = request_data['name']
    if 'email' in request_data:
        email = request_data['email']
    if 'age' in request_data:
        age = request_data['age']

    client = Client(name=name, age=age, email=email)
    session.add(client)
    session.commit()
    return jsonify(status='Ok')


@app.route('/clients/<int:id>', methods=['PATCH'])
def update_client(id):
    request_data = request.get_json()
    if 'name' in request_data:
        session.query(Client).filter(Client.id == id).update({"name": request_data['name']},
                                                             synchronize_session="fetch")
    if 'email' in request_data:
        session.query(Client).filter(Client.id == id).update({"email": request_data['email']},
                                                             synchronize_session="fetch")
    if 'age' in request_data:
        session.query(Client).filter(Client.id == id).update({"age": request_data['age']}, synchronize_session="fetch")
    session.commit()

    return jsonify(status='Ok')


@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    from sqlalchemy import delete
    stmt = delete(Client).where(Client.id == id).execution_options(synchronize_session="fetch")
    session.execute(stmt)
    session.commit()

    return jsonify(status='Ok')
