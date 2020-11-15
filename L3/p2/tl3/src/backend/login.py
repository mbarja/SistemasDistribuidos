#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import uuid
import logging
from db_handler import Database
from http import cookies

cgitb.enable()
logger = logging.getLogger()
print("Content-Type: application/json;charset=utf-8")
print()

def logout(cookie):
    try:
        if cookie is None:
            logger.error('COOKIE IS NONE')
            return {'error': True}

        key = cookie.get('session_key').value
        value = cookie.get('session_value').value
        logger.error("key: " + key)
        logger.error("value: " + value)
        database = Database.instance()
        database.delete_cookie(key,value)
        return{'logout':True}

    except:
        return {'error': True}


def login():
    try:
        form = cgi.FieldStorage()
        usuario= form.getvalue('username')
        logger.error('usuario: '+usuario)
        password = form.getvalue('password')
        logger.error('password: ' + password)
        database = Database.instance()
        if not database.validar_credenciales(usuario, password):
            logger.error('credenciales invalidas')
            if not database.validar_usuario(usuario):
                logger.error('No existe usuario')
                return {'error':True, 'usuario': True}
            else:
                logger.error('Clave invalida')
                return {'error': True, 'password':True}
        else:
            if database.exists_cookie(usuario):
                cookie =database.get_cookie(usuario)
            else:
                cookie = uuid.uuid4().hex
                database.insert_cookie(usuario, cookie)
            return {'error': False, 'cookie': cookie}
    except:
        return {'error': True}

if os.environ['REQUEST_METHOD'] == 'GET':
    cookie = cookies.SimpleCookie(os.environ['HTTP_COOKIE'])
    logger.error("login get")
    response = logout(cookie)

if os.environ['REQUEST_METHOD'] == 'POST':
    response = login()
if not response:
    response = {}

print(json.JSONEncoder().encode(response))