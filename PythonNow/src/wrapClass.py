#!/usr/bin/env python

#python2 is compatible with python3
from __future__ import print_function
#import sys
from time import time,ctime,sleep
#'div' operator only exists in python2, python3 uses 'truediv' instead
from operator import add,sub,mul,truediv

## get python version
#_pyVer = sys.version_info
## python2?
#_is_py2 = (_pyVer[0] == 2)
## python3?
#_is_py3 = (_pyVer[0] == 3)
#print(_pyVer)

class capOpen(object):
    'Wrapping a File Object'
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return 'self.file'

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)


def testOpen():
    f = capOpen('/home/demonlee/Downloads/terminal/ls.txt', 'w')
    f.write('Hello, my name is DemonLee!\n')
    f.write('Nice to meet you!\n')
    f.close()
    print('f==%s'%f)
    f1 = capOpen('/home/demonlee/Downloads/terminal/ls.txt')
    allLines = f1.readlines()
    for eachLine in allLines:
        print(eachLine, end='')


class wrapTime(object):
    'wrapping standard types:time'
    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if type(t_type) != type('') or t_type[0] not in 'cma':
            raise(TypeError("argument of 'c','m', 'a'"))
        return eval('self._%s__%stime'%(self.__class__.__name__, t_type[0]))

    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return 'self.__data'

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, attr):
        self.__atime = time()
        return getattr(self.__data, attr)


def testWrapTime():
    wtobj = wrapTime(932)
    print('ctime==', wtobj.gettimestr('c'))
    print('atime==', wtobj.gettimestr('a'))
    print('mtime==', wtobj.gettimestr('m'))
    sleep(2)
    print('------wtobj==', wtobj)
    print('ctime==', wtobj.gettimestr('c'))
    print('atime==', wtobj.gettimestr('a'))
    print('mtime==', wtobj.gettimestr('m'))
    sleep(3)
    print("------wtobj set------")
    wtobj.set('Time is up!')
    print('ctime==', wtobj.gettimestr('c'))
    print('atime==', wtobj.gettimestr('a'))
    print('mtime==', wtobj.gettimestr('m'))


def testChkType(data):
    if type(data) == int:
        #if type(data) == type(0):
        print('you entered an integer!')
    elif type(data) == str:
        #elif type(data) == type(''):
        print('you entered an string!')
    elif type(data) == float:
        #elif type(data) == type(123.123):
        print('you entered an float!')
    else:
        raise(TypeError('only integer, string or float!'))

def testOperator():
    vec1 = [30,50]
    vec2 = [3,5,8]
    opType = {add, sub, mul, truediv}
    for iOp in opType:
        for num1 in vec1:
            for num2 in vec2:
                print('%s(%d,%d)=%d'%(iOp.__name__, num1, num2, iOp(num1, num2)))

if '__main__' == __name__:
    # testOpen()
    testWrapTime()
else:
    print("---being imported by another module---")

