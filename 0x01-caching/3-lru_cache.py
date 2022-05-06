#!/usr/bin/env python3
'''Least Recently Used caching Policy
'''

from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    '''Represents an object that allows storing and
    retrieving items from a dictionary with a LRU
    removal mechanism when the limit is reached.
    '''
    def __init__(self) -> None:
        '''Initializes the Class
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds item to the Cache
        '''
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(True)
            print('DISCARD:', first_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        '''Retrieves an Item by key
        '''
        if key is None or key not in self.cache_data.keys():
            return None
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
