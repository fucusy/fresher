from lib.models import push

__author__ = 'user'

p = push.Push()
need_pushes = p.get_pushes(0,100)
for need_push in need_pushes:
    print "have notice need push\n"
    need_push.send_mail()
    need_push.set_pushed()