__author__ = 'user'
import MySQLdb
import smtplib

from email.mime.text import MIMEText

import config
import user
class Push:

    push_id = ''
    user_id = ''
    title = ''
    content = ''
    date = ''
    is_pushed = ''
    website_id = ''
    content_url = ''

    connection = ''
    cursor = ''

    def __init__(self):
        self.connection = MySQLdb.connect(config.host, config.user, config.password \
                                          , config.db, charset = config.charset)
        self.cursor = self.connection.cursor()



    def version(self):
        self.cursor.execute("SELECT VERSION()")
        return self.cursor.fetchone()

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