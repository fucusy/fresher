import push, base, user_website


__author__ = 'user'

import urllib2
import MySQLdb

class Website(base.Base):
    website_id = ""
    website_addr = ""
    now_page = None

    def get_records(self,offset, rows):
        records_list = []
        query = "SELECT `website_id`, `website_address` " \
                " FROM `website` "\
                " LIMIT %d,%d" % (offset, rows);
        self.cursor.execute(query)

        datas = self.cursor.fetchall()
        for data in datas:
            if data != None:
                p = Website()
                p.website_id = data[0]
                p.website_addr = data[1]
                records_list.append(p)
        return records_list

    """Return the newest website history

    """
    def get_history(self):
        if self.website_id is None:
            return None
        query = "select `content` from `website_history`" \
                " where `website_id` = %d " \
                " order by `date` desc" \
                " limit 1" % self.website_id

        self.cursor.execute(query)
        return self.cursor.fetchone()

    """Insert record into website_history table

    """
    def insert_history(self, history, date):
        if self.website_id is None:
            return None
        query = "insert into `website_history`(`website_id`,`content`,`date`)" \
                " values ( %d, '%s', '%s' )" % (self.website_id, history, date)
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except MySQLdb.Error, e:
            print "fail to insert the history"
            print "Error %d: %s" % (e.args[0],e.args[1])
            self.connection.rollback()

    """Return now page content
    """
    def get_now_page(self):
        if not self.now_page:
            search_request = urllib2.Request( self.website_addr )
            search_response = urllib2.urlopen( search_request )
            page = search_response.read()
            for i in range(0,10):
                page  = page.replace( str(i),"")
            self.now_page = page.replace("'","\\'")
        return self.now_page

    """Return whether any change
    """
    def is_different(self):
        return self.get_now_page() != self.get_history()

    """Insert data into push table
    """
    def insert_push(self):
        uw = user_website.UserWebsite()
        userids = uw.get_user_ids_by_website_id(self.website_id)
        for id in userids:
            p = push.Push()
            p.website_id = self.website_id
            p.user_id = id
            p.title = self.website_addr
            p.content = self.website_addr
            p.date = "2014-10-17"
            p.website_id = self.website_id
            p.content_url = ""
            p.insert()
