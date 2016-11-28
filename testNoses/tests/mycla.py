#!/usr/bin/env python

class noseClass(object):
    def __init__(self):
        print("nose class init")
        self.value = "Some value"

    def isOk(self):
        print("test nose class isOk")
        return True

    def raise_exc(self, val):
        print("test nose class raise_exc")
        raise KeyError(val)

