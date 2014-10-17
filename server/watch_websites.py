__author__ = 'user'

from models.website import *

start = 0
count = 100
website_list = Website().get_records(start, count)
while website_list:
    for site in website_list:
        if site.is_different():
            site.insert_push()
    start += count
    website_list = Website().get_records(start, count)
