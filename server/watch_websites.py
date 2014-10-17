__author__ = 'user'

search_request = urllib2.Request( searchUrl, search_data )
search_response = urllib2.urlopen( search_request )
print search_response.read()
