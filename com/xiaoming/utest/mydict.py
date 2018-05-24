# -*- coding: UTF-8 -*-
# author fangxiaoming01

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Dict' object %s" % key)

    def __setattr__(self, key, value):
        self[key] = value
