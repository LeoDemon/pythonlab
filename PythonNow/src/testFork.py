#!/usr/bin/env python

import os
from time import sleep

def forkPro():
    print('-'*10 + 'begin forkPro' + '-'*10)
    ret = os.fork()
    if 0 == ret:
        print('*'*10+'This is child process'+'*'*10)
        f=os.popen('uname -a')
        data=f.readline()
        f.close()
        print('This is %s'%data)
        sleep(10)
        print('*'*10+'child process is over'+'*'*10)
    else:
        print('*'*10+'This is parent process'+'*'*10)
        os.wait()
        print('*'*10+'parent process is over'+'*'*10)
    print('-'*10 + 'end forkPro' + '-'*10)


if '__main__' == __name__:
    forkPro()
else:
    print('testFork.py is imported by another module...')

