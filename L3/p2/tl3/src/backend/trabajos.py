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
import datetime
from db_handler import Database

cgitb.enable()
logger = logging.getLogger()
database = Database.instance()

print("Content-Type: application/json;charset=utf-8")
print()


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


def query_trabajos(id_usuario):
    trabajos = []
    for trabajo in database.get_trabajos(id_usuario):
        fechaInicio = trabajo.get('fecha_inicio').strftime("%d/%m/%Y")
        fechaFin = trabajo.get('fecha_fin').strftime("%d/%m/%Y")
        trabajo.pop('_sa_instance_state', None)
        trabajo.pop('fecha_inicio')
        trabajo['fecha_inicio'] = fechaInicio
        trabajo.pop('fecha_fin')
        trabajo['fecha_fin'] = fechaFin
        trabajos.append(trabajo)
    return trabajos


def create_trabajo(id_usuario):
    try:

        form = cgi.FieldStorage()
        fechaFin = datetime.datetime.strptime(form.getvalue('fecha_fin'), "%d/%m/%Y").strftime("%Y-%m-%d")
        fechaInicio = datetime.datetime.strptime(form.getvalue('fecha_inicio'), "%d/%m/%Y").strftime("%Y-%m-%d")
        trabajo = Trabajo(
            id_usuario,
            form.getvalue('lugar'),
            fechaInicio,
            fechaFin,
            form.getvalue('cargo'),
            form.getvalue('observacion')
        )
        logger.error(trabajo.lugar)
        logger.error(trabajo.fecha_inicio)
        logger.error(trabajo.fecha_fin)
        logger.error(trabajo.cargo)
        logger.error(trabajo.observacion)
        database.insert_trabajo(trabajo)
        return {'error': False}
    except:
        return {'error': True}

if 'HTTP_COOKIE' in os.environ:
    cookie = cookies.SimpleCookie(os.environ['HTTP_COOKIE'])
    logger.error('HAY COOKIES')

    if cookie is None:
        logger.error('COOKIE IS NONE')
        response = {'error': True, 'credenciales': True}

    key = cookie.get('session_key').value
    value = cookie.get('session_value').value
    logger.error("key: " + key)
    logger.error("value: " + value)
    if not database.exists_cookie(key):
        logger.error('Error cookie not in database')
        response = {'error': True, 'credenciales': True}
    else:
        id_usuario = database.get_id_usuario(key)
        if os.environ['REQUEST_METHOD'] == 'GET':
            logger.error("get trabajos")
            response = query_trabajos(id_usuario)

        if os.environ['REQUEST_METHOD'] == 'POST':
            response = create_trabajo(id_usuario)
        if not response:
            response = {}
else:
    logger.exception('el environment no tiene la cookie')
    response = {'error': True, 'credenciales': True}
logger.error(response)
print(json.JSONEncoder().encode(response))
