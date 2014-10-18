import base

__author__ = 'user'


class User(base.Base):
    user_id = ''
    email_addr = ''
    date = ''


    def get_email_addr_by_user_id(self, user_id):
        query = "select `email_addr` from `user` where `user_id` = \"%s\""%user_id
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except:
            print "fail to get email addr"
            self.connection.rollback()

