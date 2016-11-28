#file_name: funcPointer.py
#learning how to use function pointer


def convertFunc(funcPos, funcArgs):
    'convert funcArgs by function[funcPos]!'
    return [funcPos(eachArg) for eachArg in funcArgs]

def mult3(arg):
    return arg*3

def main():
    inParams=[3.6, 'hello,world!', 300]
    print('in---%s'%inParams)
    outParams = convertFunc(mult3, inParams)
    print('out---%s'%outParams)


if '__main__' == __name__:
    main()
else:
    print('---being imported by another module---')

