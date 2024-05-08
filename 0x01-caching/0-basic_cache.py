#!/usr/bin/python3
"""
This module contains the class BasicCache that inherits
from BaseCaching and is a caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    This class acts as a caching system
    """

    def put(self, key, item):
        """
        This method assigns an item to the given key
        in the dictionary, self.cache_data
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to key in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
