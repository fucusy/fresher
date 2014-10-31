__author__ = 'user'
import push, base, user_website
import urllib2
import MySQLdb
from bs4 import BeautifulSoup
from datetime import datetime



class Website(base.Base):
    website_id = ""
    website_addr = ""
    now_page = ""
    def insert(self,addr):
        query = "INSERT INTO `website`(`website_address`)" \
                " VALUES ( '%s' )" % (addr)
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except MySQLdb.Error, e:
            print "fail to insert the website"
            print "Error %d: %s" % (e.args[0],e.args[1])
            self.connection.rollback()

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


    def has_no_history(self):
        return self.get_history() == None

    def initialize(self):
        his  = self.get_now_page()
        self.insert_history(his, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
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
        data = self.cursor.fetchone()
        history = None
        if data:
            history = data[0]
        return history

    """Insert record into website_history table

    """
    def insert_history(self, history, date):
        if self.website_id is None:
            return None
        query = "insert into `website_history`(`website_id`,`content`,`date`)" \
                " values ( %d, \"%s\", \"%s\" )" % (self.website_id, history, date)
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
            soup = BeautifulSoup(str(page))

            content = ""
            for tag in soup.findAll('a', href=True):
                content = tag.get_text().strip()
                if len(content) > 0:
                    content = str(tag).replace("\"","'") + "\n"
                    self.now_page += content
        return self.now_page

    """Return whether any change
    """
    def is_different(self):
        return self.get_different() != ""

    """Get the difference as content send out
    """
    def get_different(self):

        history = self.get_history()
        if not history:
            history = ""
        soup_his = BeautifulSoup(history)
        his_link_list =  soup_his.find_all('a')

        his_link_dic = {}
        for link in his_link_list:
            text = link.get_text().strip()
            href = link["href"]
            his_link_dic[text] = href


        soup_now = BeautifulSoup(self.get_now_page())
        now_link_list =  soup_now.find_all('a')

        now_link_dic = {}
        for link in now_link_list:
            text = link.get_text().strip()
            href = link["href"]
            now_link_dic[text] = href

        differ = []
        for now_title in now_link_dic.iterkeys():
            if now_title not in his_link_dic.iterkeys():
                append = ""
                append += "<a href='"
                append += self.website_addr.rstrip('/')
                append += str(now_link_dic.get(now_title))
                append += "'>"
                append += now_title
                append += "</a>"
                differ.append( append )
        differ_content = ""
        for d in differ:
            d += "\n"
            differ_content += d
        return differ_content
    """Insert data into push table
    """
    def insert_push(self):
        uw = user_website.UserWebsite()
        userids = uw.get_user_ids_by_website_id(self.website_id)
        for id in userids:
            p = push.Push()
            p.website_id = self.website_id
            p.user_id = id
            p.title = self.website_addr + " has new notice"
            content = "the newest notice is :\n"
            content += self.get_different()
            p.content = content
            p.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            p.website_id = self.website_id
            p.content_url = ""
            p.insert()
