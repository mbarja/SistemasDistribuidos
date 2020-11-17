#!/usr/bin/python3
import os
import cgi
from http import cookies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, Integer, MetaData, Date, ForeignKey, tuple_
import logging


logger = logging.getLogger()

class Database:

    __instance = None

    @staticmethod
    def instance():
        if (Database.__instance == None):
            Database.__instance = Database()
        return Database.__instance

    def __init__(self):
        if (Database.__instance is not None):
            return Database.__instance
        db_string = "postgres://admin:admin@tl3_db:5432/tl3"
        self.db = create_engine(db_string, echo=False)
        self.meta = MetaData(self.db)

        self.cookies = Table(
                        'cookies',
                        self.meta,
                        Column('key', String, primary_key=True),
                        Column('value', String)
                       )
        self.users = Table(
                        'users',
                        self.meta,
                        Column('id', Integer, primary_key=True),
                        Column('name', String),
                        Column('username', String),
                        Column('age', Integer),
                        Column('password', String),
                    )
        self.trabajos = Table(
                        'trabajos',
                        self.meta,
                        Column('id', Integer, primary_key=True),
                        Column('id_usuario', Integer),
                        Column('lugar', String),
                        Column('fecha_inicio', Date),
                        Column('fecha_fin', Date),
                        Column('cargo', String),
                        Column('observacion', String)
        )


    def exists_cookie(self, key):
        logger.error('exist_cookie')
        result = self.meta.tables["cookies"]
        cookie_row = result.select().where(result.c.key==key)
        cookies_rs = self.db.execute(cookie_row)
        return cookies_rs.rowcount == 1

    def get_cookie(self, key):
        result = self.meta.tables["cookies"]
        cookie_row = result.select().where(result.c.key==key)
        cookie_rs = self.db.execute(cookie_row)
        if (cookie_rs.rowcount != 0):
            cookie = cookie_rs.first()
            return [cookie[1]]
        else:
            return []

    def insert_cookie(self, key, value):
        statement = self.cookies.insert().values(key=key, value=value)
        self.db.execute(statement)

    def delete_cookie(self, key, value):
        deleteStmt = self.cookies.delete().where(self.cookies.c.key == key)
        self.db.execute(deleteStmt)

    def validar_credenciales(self, username,password):
        result = self.meta.tables["users"]
        user_row = result.select().where(result.c.username == username).where(result.c.password == password)
        user_rs = self.db.execute(user_row)
        return user_rs.rowcount == 1

    def validar_usuario(self, username):
        result = self.meta.tables["users"]
        user_row = result.select().where(result.c.username == username)
        user_rs = self.db.execute(user_row)
        return user_rs.rowcount == 1

    def get_id_usuario(self, username):
        result = self.meta.tables["users"]
        user_row = result.select().where(result.c.username == username)
        user_rs = self.db.execute(user_row)
        if (user_rs.rowcount != 0):
            user = user_rs.first()
            return user[0]
        else:
            return 0

    def get_trabajos(self, id_usuario):
        logger.error('get_trabajos')
        result = self.meta.tables["trabajos"]
        trabajos_row = result.select().where(result.c.id_usuario == id_usuario)
        trabajos_rs = self.db.execute(trabajos_row)
        if (trabajos_rs.rowcount != 0):
            d, a = {}, []
            for rowproxy in trabajos_rs:
                # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
                for column, value in rowproxy.items():
                    # build up the dictionary
                    d = {**d, **{column: value}}
                a.append(d)
            return a
        else:
            logger.error("no hay trabajos")
            return []

    def insert_trabajo(self, trabajo):
        statement = self.trabajos.insert().values(id_usuario=trabajo.id_usuario, lugar=trabajo.lugar, fecha_inicio=trabajo.fecha_inicio,
                                                  fecha_fin=trabajo.fecha_fin, cargo=trabajo.cargo, observacion=trabajo.observacion)
        logger.error(statement)
        self.db.execute(statement)
