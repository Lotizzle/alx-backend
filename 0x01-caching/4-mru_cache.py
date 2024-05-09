#!/usr/bin/python3
"""
This module contains a class MRUCache that inherits
from BaseCaching and is a caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    This class implements the MRU approach for caching
    """

    def __init__(self):
        """Initializes"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                most_recent_key = next(iter(self.cache_data))
                print("DISCARD: {}".format(most_recent_key))
                del self.cache_data[most_recent_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item for a key """
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end of the OrderedDict
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
