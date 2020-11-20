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
import uuid
import datetime

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

trabajos_table = Table('trabajos', metadata,
   Column('id', Integer, primary_key=True),
   Column('id_usuario', Integer),
   Column('lugar', String),
   Column('fecha_inicio', Date),
   Column('fecha_fin', Date),
   Column('cargo', String),
   Column('observacion', String),
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

class Trabajo(declarative_base()):
    __tablename__ = 'trabajos'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer)
    lugar = Column(String)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    cargo = Column(String)
    observacion = Column(String)

    def __init__(self, id_usuario, lugar, fecha_inicio, fecha_fin, cargo, observacion):
        self.id_usuario = id_usuario
        self.lugar = lugar
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.cargo = cargo
        self.observacion = observacion


def exist_cookie(key, value):
    query = session.query(Cookie).filter(Cookie.key == key).filter(Cookie.value == value).first()
    if not query:
        return False
    else:
        return True


@app.route("/trabajos/")
def index():
    return render_template("index.html")

@app.route("/trabajos/get_trabajos", methods=["GET"])
def get_trabajos():
    cookie = request.cookies
    key = cookie.get('session_key')
    value = cookie.get('session_value')
    if not exist_cookie(key,value):
        print('Error cookie not in database')
        data = {'error': True, 'credenciales': True}
    else:
        trabajos = []
        usuario = session.query(User).filter(User.username == key).first()
        queryTrabajos = session.query(Trabajo).filter(Trabajo.id_usuario == usuario.id).all()
        for u in queryTrabajos:
            trabajo = u.__dict__
            trabajo.pop('_sa_instance_state', None)
            fechaInicio = trabajo.get('fecha_inicio').strftime("%d/%m/%Y")
            fechafinDB = trabajo.get('fecha_fin')
            fechaFin = None
            if(fechafinDB):
                fechaFin = fechafinDB.strftime("%d/%m/%Y")
            trabajo.pop('_sa_instance_state', None)
            trabajo.pop('fecha_inicio')
            trabajo['fecha_inicio'] = fechaInicio
            trabajo.pop('fecha_fin')
            trabajo['fecha_fin'] = fechaFin
            trabajos.append(trabajo)
        data = trabajos

    return make_response(jsonify(data), 200)

@app.route("/trabajos/create_trabajo", methods=["POST"])
def post_trabajo():
    print(" === Crear TRABAJO || post_trabajo ")
    print(request.get_data())
    cookie = request.cookies
    key = cookie.get('session_key')
    value = cookie.get('session_value')
    print('key: ' + key)
    print('value: ' + value)
    if not exist_cookie(key, value):
        print('Error cookie not in database')
        data = {'error': True, 'credenciales': True}
    else:
        usuario = session.query(User).filter(User.username == key).first()
        fechaFin = None
        observacion = None
        if request.form.get('fecha_fin') != '':
            fechaFin = datetime.datetime.strptime(request.form.get('fecha_fin'), "%d/%m/%Y").strftime("%Y-%m-%d")
        if request.form.get('observacion') != '':
            observacion = request.form.get('observacion')
        fechaInicio = datetime.datetime.strptime(request.form.get('fecha_inicio'), "%d/%m/%Y").strftime("%Y-%m-%d")
        trabajo = Trabajo(
            usuario.id,
            request.form.get('lugar'),
            fechaInicio,
            fechaFin,
            request.form.get('cargo'),
            observacion
        )
        session.add(trabajo)
        session.commit()
        data = {'error': False}
    return make_response(jsonify(data), 200)

@app.route("/trabajos/editar_trabajo", methods=["POST"])
def post_editar_trabajo():
    print(" === Editar TRABAJO || post_trabajo ")
    print(request.get_data())
    cookie = request.cookies
    key = cookie.get('session_key')
    value = cookie.get('session_value')
    print('key: ' + key)
    print('value: ' + value)
    if not exist_cookie(key, value):
        print('Error cookie not in database')
        data = {'error': True, 'credenciales': True}
    else:
        idTrabajo = request.form.get('idTrabajo')
        fechaFin = None
        observacion = None
        if request.form.get('fecha_fin') != '':
            fechaFin = datetime.datetime.strptime(request.form.get('fecha_fin'), "%d/%m/%Y").strftime("%Y-%m-%d")
        if request.form.get('observacion') != '':
            observacion = request.form.get('observacion')
        fechaInicio = datetime.datetime.strptime(request.form.get('fecha_inicio'), "%d/%m/%Y").strftime("%Y-%m-%d")
        session.query(Trabajo).filter(Trabajo.id == idTrabajo).update({'fecha_inicio': fechaInicio, 'fecha_fin':fechaFin, 'lugar':request.form.get('lugar'),
                                                                       'cargo': request.form.get('cargo'), 'observacion':observacion})
        session.commit()
        print(request.get_data())
        print(request.form)
        data = {'error': False}
    return make_response(jsonify(data), 200)

@app.route("/trabajos/eliminar", methods=["POST"])
def post_eliminar():
    print(" === POST_TRABAJOS ")
    cookie = request.cookies
    key = cookie.get('session_key')
    value = cookie.get('session_value')
    print('key: ' + key)
    print('value: ' + value)
    if not exist_cookie(key, value):
        print('Error cookie not in database')
        data = {'error': True, 'credenciales': True}
    else:
        idTrabajo = request.form.get('idTrabajo')
        query = session.query(Trabajo).filter(Trabajo.id == idTrabajo).delete()
        session.commit()
        print(query)
        data = {'delete': True}
        return make_response(jsonify(data), 200)


if __name__ == '__main__':
    print(f"Login microservice runnning in port {PORT}")
    app.run(host=HOST, port=PORT, debug=True)