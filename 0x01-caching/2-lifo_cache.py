#!/usr/bin/python3
"""
This module contains the class LIFOCache that inherits
from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    This class implements the LIFO approach for caching
    """

    def __init__(self):
        """Initializes"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = next(reversed(self.cache_data))
                print("DISCARD: {}".format(last_key))
                self.cache_data.popitem(last=False)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item for a key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
