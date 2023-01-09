#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Persistencia_factory, Persistencia_usuari_sqlite

"""
    Persistencia_factory_mySql.py
    Classe que defineix la interficie amb la fàbrica de persistencia per a mySql.
"""


class Persistencia_factory_sqLite(Persistencia_factory.Persistencia_factory):
    def __init__(self, host, path):
        self.host = host
        self.path = path

    def get_Persistencia_usuari_factory(self):
        return Persistencia_usuari_sqlite.Persistencia_usuari_sqlite(
            self.host,
            self.path,
        )

