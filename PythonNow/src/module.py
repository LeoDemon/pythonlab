#module.py

def module_func():
    import sys
    print 'The command line arguments are:'
    for i in sys.argv:
        print i

    print '\nThe Python Path is: ', sys.path, '\n'

def sayhi():
    print 'Hey,Guy! Welcome to Python!'

version = 0.1

if __name__ == '__main__':
    sayhi()
else:
    print 'being imported from another module...'
