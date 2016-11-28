#!/usr/bin/python3.5

import logging
import sys

'''This is for function test!
...May you can get funny from python!'''

logging.debug("---logger.debug...")
logging.warning("---logger.warning...")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', filename='./mypy.log', filemode='a')
logging.debug("---logger.debug 2...")

#global parameters
def printMax():
    global a, b
    if a > b:
        print (a, "is maxinum")
    else:
        print (b, "is maxinum")
        a = 30

#default parameters
def printMsg(msg="hey", times=1):
    print (msg * times)

#key parameters
def printKey(x, y=123, z=678):
    print ('x==', x, ", y==", y, ", z==", z)

#return value
def funcNon():
    pass #empty block code

def funcNon2():
    return None  #equals no return value

#DocStrings
def funcRet():
    '''Test return value function for python.

    If you have no return value, it equals return None.'''
    return "back to you"

def funcArgs(x,*yy):
    total=0
    for y in yy:
        total += pow(y,x)
        return total

def make_repeater(n):
    return lambda s:s*n
twice=make_repeater(3)

a = 11
b = 12
def test_now():
    printMax()
    print ("|||a==", a)
    printMax()
    printMsg()
    printMsg("Hello")
    printMsg("Hello World! ", 3)
    printKey(27)
    printKey(36, z=989)
    printKey(y=129, x=800)
    funcNon()
    funcNon2()
    msg = funcRet()
    print ("return value==",msg)
    #print DocStrings
    print (funcRet.__doc__)
    print ('FuncArgs(2,3,4)==', funcArgs(2,3,4,5))
    print ('FuncArgs(10,2)==', funcArgs(2,10))
    print (twice('Hi,'))
    print (twice(10))

if  __name__ == '__main__':
    test_now()
else:
    print('This is being imported from another module...__name__==[%s]'%__name__)

