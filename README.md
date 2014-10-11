fresher
=======

follow publishing notice websites,  receive the info at the first time on mobile phone client.

famirily product, 速推, 狠狠推, 追信


chrome extension function:
    using the chrome add notices website address.


implemented method:
	1.when user add the extension, retrive user id from server,
	user can sync the user id between mobile client and computer through
	2D code.
	2.when user add a website, the chrome extension send the website address 
	to server, the server check the website address is valid and check the address
	whether exists in the website address table, if not add it to the database
	and add user id and website id to the user to website address table.
    
    now the chrome extension function is finished.



mobile phone client or chrome client:
    receive the notification of website notice
    display the notice

implemented method:
    android client: google cloud message        https://developer.android.com/google/gcm/index.html
    ios client:  Local and Push Notifications   https://developer.apple.com/notifications/

server function:
    watch the website address added by user
    if website offer notice add then the notice to website notice queue

implemented method:
    create tables, 
        user table, user id, register date,
        website table, website id, website address, website domain name
        user to website table, user id, website id, follow date
    script: to watch the website in website table and send notification to mobile client
    
    
	