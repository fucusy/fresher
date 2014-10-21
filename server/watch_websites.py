__author__ = 'user'
import time
from lib.models.website import Website

start = 0
count = 100
website_list = Website().get_records(start, count)
while website_list:
    for site in website_list:
        if site.has_no_history():
            site.initialize()
        else:
            if site.is_different():
                print site.website_addr + " changes"
                print site.get_different()
                site.insert_push()
                site.insert_history(site.get_now_page(), time.strftime("%Y-%m-%d %H:%M:%S") )

    start += count
    website_list = Website().get_records(start, count)
