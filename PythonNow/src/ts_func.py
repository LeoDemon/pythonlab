#file_name: ts_func.py
#description: for learning yield and closure

from time import ctime, sleep

##for yield
def yield_counter(start_at=0):
    count=start_at
    print('count1==%s'%str(count))
    while count>0:    # here cann't using [IF] instead of [WHILE]
        val=(yield count)
        print('count2==%s'%str(count))
        print('val==%s'%str(val))
        if val is not None:
            count=val
        else:
            count-=1


##for closure
def clos_counter(start_at=0):
    count=[start_at]
    def incr_counter():
        count[0]+=1
        return count[0]
    return incr_counter


##for decoration
def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s() called'%(ctime(), func.__name__))
        return func()
    return wrappedFunc

@tsfunc
def foo():
    print('---in foo---')
    pass


def main():
    foo()
    sleep(3)
    for i in range(2):
        sleep(1)
        foo()

def global_var_func():
    global a,b
    print('a==%d,b==%d'%(a,b))
    a,b=1,2
    print('a==%d,b==%d'%(a,b))

a,b=0,1

if '__main__' == __name__:
    global_var_func()
else:
    print('being imported by another module...')


