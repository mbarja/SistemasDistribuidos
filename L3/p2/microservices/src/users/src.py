from flask import (
    Flask,
    render_template,
    make_response,
    jsonify,
    request,
)
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

PORT = 5000
HOST = '0.0.0.0'

json = {
    "languajes": {
        "es": "Spanish",
        "en": "English",
        "fr": "French",
    },
    "colors": {
        "r": "Red",
        "g": "Green",
        "b": "Blue",
   }
}

#db_string = "postgres://admin:admin@127.0.0.1:5550/microservices"
db_string = "postgres://admin:admin@tl3_ms_db:5432/tl3"

engine = create_engine(db_string, echo=False)

metadata = MetaData()

users_table = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
     Column('username', String),
     Column('age', Integer),
     Column('password', String),
)

cookies_table = Table('cookies', metadata,
    Column('key', String, primary_key=True),
    Column('value', String),
)

metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class User(declarative_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    age = Column(Integer)
    password = Column(String)

    def __init__(self, name, age, username, password):
        self.name = name
        self.age = age
        self.username = username
        self.password = password

class Cookie(declarative_base()):
    __tablename__ = 'cookies'

    key = Column(String, primary_key=True)
    value = Column(String)

    def __init__(self, key, value):
        self.key = key
        self.value = value


def exist_cookie(key, value):
    query = session.query(Cookie).filter(Cookie.key == key).filter(Cookie.value == value).first()
    if not query:
        return False
    else:
        return True


@app.route("/users/")
def index():
    return render_template("users.html")

@app.route("/users/get_users", methods=["GET"])
def get_users():
    cookie = request.cookies
    key = cookie.get('session_key')
    value = cookie.get('session_value')
    if not exist_cookie(key,value):
        print('Error cookie not in database')
        data = {'error': True, 'credenciales': True}
    else:
        users = []
        for u in session.query(User).all():
            user = u.__dict__
            user.pop('_sa_instance_state', None)
            users.append(user)
        data = users
    return make_response(jsonify(data), 200)

@app.route("/users/create_user", methods=["POST"])
def post_user():
    cookie = request.cookies
    key = cookie.get('session_key')
    value = cookie.get('session_value')
    if not exist_cookie(key, value):
        print('Error cookie not in database')
        data = {'error': True, 'credenciales': True}
    else:
        user = User(
                request.form.get('name'),
                request.form.get('age'),
                request.form.get('username'),
                request.form.get('password')
                )
        session.add(user)
        session.commit()
        data = {'error': False}
    return make_response(jsonify(data), 200)

if __name__ == '__main__':
    print(f"Users microservice runnning in port {PORT}")
    app.run(host=HOST, port=PORT, debug=True)
