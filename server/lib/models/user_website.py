import base

__author__ = 'user'


class UserWebsite(base.Base):

    def get_user_ids_by_website_id(self,website_id):
        user_list = []
        query = "select `user_id` from `user_website`" \
                " where `website_id` = %d " % website_id
        self.cursor.execute(query)

        datas = self.cursor.fetchall()
        for data in datas:
            user_list.append(data[0])
        return user_list