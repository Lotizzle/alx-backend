#!/usr/bin/python3
"""
This module contains the class BasicCache that inherits
from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class acts as a caching system
    """

    def __init__(self):
        """Intializes"""
        super().__init__()

    def put(self, key, item):
        """
        This method assigns an item to the given key
        in the dictionary, self.cache_data
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
