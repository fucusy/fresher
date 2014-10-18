__author__ = 'user'
import time
from lib.models.website import Website

start = 0
count = 100
website_list = Website().get_records(start, count)
while website_list:
    for site in website_list:
        if site.is_different():
            site.insert_history(site.get_now_page(), time.strftime("%Y-%m-%d %H:%M:%S") )
            site.insert_push()
    start += count
    website_list = Website().get_records(start, count)
