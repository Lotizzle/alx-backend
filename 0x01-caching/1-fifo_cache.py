#!/usr/bin/python3
"""
This module contains the class FIFOCache that inherits
from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class implements the FIFO approach for caching
    """

    def __init__(self):
        """Initializes"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                print("DISCARD:{}".format(first_item))
                del(self.cache_data[first_item])
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the item for a key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
