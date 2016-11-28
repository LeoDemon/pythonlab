# filename: use_file.py
# writing/reading to/from a file

import time

poem = '''Programming is fun \
when the work is done.
If you wanna make your work also fun:
   use Python!
'''

filePath = '../file/poem.txt'

#f = file(filePath, 'w')
#f.write(poem)
#f.close()

try:
    f = file(filePath)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        else:
            time.sleep(1)
            print line,
except  KeyboardInterrupt:
    print 'I am leisurely, and run the Ctrl-C to terminal this process...'
else:
    print 'No exception, well done...'
finally:
    f.close()
    print 'Cleaning up...closed the file'


