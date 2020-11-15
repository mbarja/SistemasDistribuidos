#!/usr/bin/python3
import os
import cgi
import cgitb
import json
from http import cookies
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging


from db_handler import Database

cgitb.enable()
logger = logging.getLogger()

print("Content-Type: application/json;charset=utf-8")
print()

db_string = "postgres://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)

metadata = MetaData()

users_table = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
     Column('username', String),
     Column('age', Integer),
     Column('password', String),
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


def query_users():
    users = []
    for u in session.query(User).all():
        user = u.__dict__
        user.pop('_sa_instance_state', None)    
        users.append(user)
    return users


def create_user():
    try:
        form = cgi.FieldStorage()
        user = User(
            form.getvalue('name'),
            form.getvalue('age'),
            form.getvalue('username'),
            form.getvalue('password')
            )
        session.add(user)
        session.commit()
        return {'error': False}
    except:
        return {'error': True}


if 'HTTP_COOKIE' in os.environ:
    cookie = cookies.SimpleCookie(os.environ['HTTP_COOKIE'])
    logger.error('HAY COOKIES')

    if cookie is None:
        logger.error('COOKIE IS NONE')
        response = {'error': True, 'credenciales':True}

    key = cookie.get('session_key').value
    value = cookie.get('session_value').value
    logger.error("key: "+key)
    logger.error("value: "+value)
    database = Database.instance()
    if not database.exists_cookie(key):
        logger.error('Error cookie not in database')
        response = {'error': True, 'credenciales':True}
    else:
        logger.error('NI IDEA')
        if os.environ['REQUEST_METHOD'] == 'GET':
            response = query_users()
        if os.environ['REQUEST_METHOD'] == 'POST':
            response = create_user()
        if not response:
            response = {}
else:
    logger.exception('el environment no tiene la cookie')
    response = {'error': True, 'credenciales': True}
print(json.JSONEncoder().encode(response))