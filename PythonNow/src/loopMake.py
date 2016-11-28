#!/usr/bin/env python


#global variables
dashesLine = '\n' + '-' * 50
#exec dictionary
exec_dict={
#for loop
'f':"""
for %s in %s:
    print(%s)
""",
#sequence while loop
's':"""
%s = 0
%s = %s
while %s < len(%s):
    print(%s[%s])
    %s = %s + 1
""",
#counting while loop
'n':"""
%s = %d
while %s < %d:
    print(%s)
    %s = %s + %d
"""
}

def loopNow():
    ltype = input('Loop type?((f)or/(w)hile)> ')
    dtype = input('Data type?((n)umber/(s)equence)> ')
    if 'n' == dtype:
        start = int(input('Starting value> '))
        stop = int(input('Ending value(non-inclusive)> '))
        step = int(input('Stepping value> '))
        seq = range(start, stop, step)
    else:
        seq = input('Enter Sequence> ')
    var = input('Iterative variable name> ')
    if 'f' == ltype:
        exec_str = exec_dict['f'] % (var, seq, var)
    else:
        if 's' == dtype:
            seqName = input('Enter Sequence name> ')
            exec_str = exec_dict['s'] % (var, seqName, seq, var, seqName, seqName, var, var, var)
        else:
            exec_str = exec_dict['n'] % (var, start, var, stop, var, var, var, step)
    print(dashesLine)
    print('Your custom-generated code:'+dashesLine)
    print(exec_str+dashesLine)
    print('Test execution of the code:'+dashesLine)
    exec(exec_str)
    print(dashesLine)

def loopMain():
    loopFlag = True
    loopTime = 0
    while loopFlag:
        loopTime += 1
        if 1 == loopTime:
            loopNow()
        else:
            loopStr = input("Continue Next Loop?(yes/no)> ")
            if 'y' == loopStr or 'yes' == loopStr:
                loopNow()
            elif 'n' == loopStr or 'no' == loopStr:
                print("loop break, exit now...")
                break
            else:
                print("[%s] is invalid input, please input again!"%loopStr)
                continue

if '__main__' == __name__:
    loopMain()
else:
    print('being imported by another module...')

