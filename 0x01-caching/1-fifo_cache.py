#!/usr/bin/env python3
'''FIFO caching
'''

from collections import OrderedDict
BaseCaching = __import__("./base_caching").BaseCaching


class FIFOCache(BaseCaching):
    '''Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    '''
    def __init__(self) -> None:
        '''Innitializes the Class
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds item to the Cache
        '''
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print('DISCARD:', first_key)
        self.cache_data.update({'{}'.format(key): item})

    def get(self, key):
        '''Retrieves an Item by key
        '''
        return self.cache_data.get(key, None)
