import time
import os


class Test(object):
    """Base class utilized to test hacks on. Test(name, **kwargs)"""
    def __init__(self, name, **kwargs):
        self.run = True
        self.name = name
        for key in kwargs.keys():
            value = kwargs.get(key)
            if isinstance(value, str):
                exec("self.{0} = '{1}'".format(key, value))
            else:
                exec("self.{0} = {1}".format(key, value))
    def mainloop_check(self, attr):
        while self.run:
            print self.name, "->", eval("self.%s" %attr)
            time.sleep(1)
    def __repr__(self):
        return "<Test: %s>" %self.name

