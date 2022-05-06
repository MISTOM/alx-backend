#!/usr/bin/env python3
'''Basic Dictionary
'''
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCaching to a Dictionary
    '''
    def __init__(self):
        '''Initialization
        '''
        self.cache_data = {}

    def put(self, key, item):
        '''Adds item to the Cache
        '''
        if key is not None and item is not None:
            self.cache_data.update({'{}'.format(key): item})

    def get(self, key):
        '''Retrieves an Item by key
        '''
        return self.cache_data.get(key)
