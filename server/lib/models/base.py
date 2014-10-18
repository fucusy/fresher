__author__ = 'user'

import MySQLdb
from ..config import config

class Base:
    connection = ''
    cursor = ''

    def __init__(self):
        self.connection = MySQLdb.connect(config.host, config.user, config.password \
                                          , config.db, charset = config.charset)
        self.cursor = self.connection.cursor()
