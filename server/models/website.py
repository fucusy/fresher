__author__ = 'user'

from ..config import config

class Website:
    website_id = ""
    website_addr = ""

    """Return the newest website history

    """
    def get_history(self):
        return None

    """Insert record into website_history table

    """
    def insert_history(self, history, date):
        return None

    """Return now page content
    """
    def get_now_page(self):
        return None

    """Return whether any change
    """
    def is_different(self):
        return True

    """Insert data into push table
    """
    def insert_push(self):
        return None