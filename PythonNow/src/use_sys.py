# filename: use_sys.py
# learning sys module

import sys

def readFine(filename):
    '''print a file to standard output'''
    try:
        f = file(filename)
        while True:
            line = f.readline()
            if 0 != len(line):
                print line,  # notice comma
            else:
                break
    except  KeyboardInterrupt:
        print 'I am leisurely, and run the Ctrl-C to terminal this process...'
    except  IOError, ie:
        print 'IOError...errno==[%s],args==[%s]' % (ie.errno, ie.args)
    else:
        print 'No exception, well done...'
    finally:
        try:
            f.close()
        except UnboundLocalError, ue:
            print 'close file error:', ue.args
        print 'Cleaning up...closed the file'

# scripts starts from here
if len(sys.argv) < 2:
    print 'No action specified, exit now!'
    sys.exit()

# i = 0
# for argv in sys.argv:
#    print 'argv[%d]==[%s]' % (i, argv)
#    i += 1

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'help':
        print '''\
        This program prints files to the standard output.
        Any number of files can be specified.
        Options include:
        --version : Prints the version number
        --help : Display this help'''
    elif option == 'version':
        print 'Version 1.0'
    else:
        print 'Unknown option'
        sys.exit()
else:
    for filename in sys.argv[1:]:
        readFine(filename)

