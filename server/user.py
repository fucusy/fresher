__author__ = 'user'

import config
import MySQLdb

class User:
    user_id = ''
    email_addr = ''
    date = ''
    connection = ''
    cursor = ''

    def __init__(self):
        self.connection = MySQLdb.connect(config.host, config.user, config.password \
                                          , config.db, charset = config.charset)
        self.cursor = self.connection.cursor()

    def get_email_addr_by_user_id(self, user_id):
        query = "select `email_addr` from `user` where `user_id` = \"%s\""%user_id
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()

        except:
            print "fail to get email addr"
            self.connection.rollback()

