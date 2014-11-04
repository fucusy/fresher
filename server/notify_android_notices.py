from lib.models import push

__author__ = 'user'

p = push.Push()
need_pushes = p.get_pushes_to_android(0,100)
for need_push in need_pushes:
    print "have notice need push\n"
    need_push.notification_android()
    need_push.set_android_pushed()
