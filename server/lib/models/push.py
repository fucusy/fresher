import user
import base
import MySQLdb
__author__ = 'user'

import smtplib
from email.mime.text import MIMEText
from ..config import config
import urllib2
import urllib

from gcm import GCM

class Push(base.Base):

    push_id = ""
    user_id = ""
    title = ""
    content = ""
    date = ""
    is_pushed = 0
    website_id = ""
    content_url = ""
    register_id =""


    def version(self):
        self.cursor.execute("SELECT VERSION()")
        return self.cursor.fetchone()

    def insert(self):
        query = "insert into `push`(`user_id`,`title`,`content`,`date`,`is_pushed`" \
                " ,`website_id`, `content_url` )" \
                " values (%d, \"%s\",\"%s\",\"%s\", %d, %d, \"%s\" ) " %(self.user_id,
                self.title, self.content, self.date, self.is_pushed, self.website_id
                ,self.content_url
                )
        self.cursor.execute(query)
        try:
            self.connection.commit()
        except MySQLdb.Error, e:
            print "fail to insert the push"

            print "Error %d: %s" % (e.args[0],e.args[1])
            self.connection.rollback()

    def set_pushed(self):
        if( self.push_id is None ):
            return False
        try:
            update = "update `push` set `is_pushed` = 1  where `push_id`= %d"%(self.push_id)
            self.cursor.execute(update)
            self.connection.commit()
        except:
            self.connection.rollback()
            print "fail to set pushed"


    def get_register_id(self):
        if not self.register_id:
            u = user.User();
            receiver = u.get_email_addr_by_user_id(self.user_id)

            query = "select `gcm_regid` from `gcm_users` where `email` = '%s'" % receiver
            try:
                self.cursor.execute(query)
                self.register_id = self.cursor.fetchone()
            except:
                print "fail to get gcm_regid addr"
                self.connection.rollback()
        return self.register_id
    def notification_android(self):
        body = self.content

        # Plaintext request
        reg_id = self.get_register_id()
        reg_id = str(reg_id)
        reg_id = reg_id[:-3]
        reg_id = reg_id[3:]
        if reg_id:
            f = { 'regId' : reg_id, 'message' : body}
            url = "http://127.0.0.1/send_message.php?%s"% urllib.urlencode(f)
            print urllib2.urlopen(url).read()

    def send_mail(self):
        if( self.push_id is None ):
            return False

        body = self.content
        msg = MIMEText(body,'html','utf-8')

        msg['Subject'] = self.title

        u = user.User();
        receiver = u.get_email_addr_by_user_id(self.user_id)


        s = smtplib.SMTP(config.mail_host, config.mail_port)
        s.login(config.mail_sender, config.mail_pwd)
        s.sendmail(config.mail_sender, receiver, msg.as_string())
        s.quit()

    def get_pushes(self,offset, rows):
        push_list = []
        query = "select `push_id`, `user_id`, `title`, `content`, `date`, `website_id`" \
                ", `content_url`, `content` \
                FROM  `push` WHERE `is_pushed` = 0" \
                " ORDER BY `date` ASC" \
                " LIMIT %d,%d" % (offset, rows);
        self.cursor.execute(query)

        datas = self.cursor.fetchall()
        for data in datas:
            if data != None:
                p = Push()
                p.push_id = data[0]
                p.user_id = data[1]
                p.title = data[2]
                p.content = data[3]
                p.date = data[4]
                p.website_id = data[5]
                p.content_url = data[6]
                p.content = data[7]
                push_list.append(p)
        return push_list

    def is_need_push(self):
        query = "select count(*) from push where is_pushed = 0"
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchone()
            print data[0]
            return data[0] > 0
        except:
            print "fail to check"
            self.connection.rollback()

    def get_next_push(self):
        push_list = self.get_pushes(0,1)
        if push_list:
            return push_list[0]