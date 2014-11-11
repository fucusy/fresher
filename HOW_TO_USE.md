The run time environment:
======

**chrome mysql software**
**apache,nginx or other web server software**
**php 5.5 or up version**
**python 2.7 and other python package** 
**Android OS 4.2 or up version**


Chrome Extension
======

the script under chrome extension directory is the chrome extension
you can directly load the directory into chrome extension, and use it
more detail refer to https://developer.chrome.com/extensions

Chrome Extension Bank-end Server
======

first you should set up a mysql database named fresher
and run the sql file named "fresher.create.sql" under the table_create_sql directory

and run the /server/php_chrome_extension_backend directory which contains php script at 127.0.0.1:8081


Android Client
======
the source file is under the android_client directory you can build it yourself
or you can install the pre-build AndroidPushNotificationsUsingGCM.apk file that 
under the /android_client/bin into you android phone

Android Client Backend
======
This module is used to send message to Android client, and it is called by next python script 
when new notice appears
,you should run the /server/php_android_backend directory which contains php script at 127.0.0.1

Server Python Script
======
the main file is under the server directory.
###First file named "watch_websites.py"
this file used to watch websites publishing notices, and save the new notice to database
###Second file named "mail_notices.py"
this file used to send new notice to user's mail
###Third file named "notify_android_notices.py"
this file used to send new notice notification to user's android phone which was registered by the same 
email address that enter at chrome extension

**you need run those python script file every 5 minutes or other interval you prefer to run the three file respectively, you can achieve this by add the crontab task on \*uix platform**
**you can run crontab -e you edit you crontab job, more detail refer to [cron](http://en.wikipedia.org/wiki/Cron)**






