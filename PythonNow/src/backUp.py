# filename: backUp.py
# using zipfile compress file and backup
import os
import time
import zipfile

def backup():
    print '---begin backup---'
    def_dir = 'D:\\downloads\\'
    today = time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    comment_str = raw_input('Enter a comment: ')
    if len(comment_str) == 0:
        tar_dir = def_dir + today + os.sep + now + '.zip'
    else:
        tar_dir = def_dir + today + os.sep + now + \
        '_' + comment_str.replace(' ', '_') + '.zip'
    if not os.path.exists(def_dir + today):
        os.mkdir(def_dir + today)
        print 'Create a new directory [%s]' % def_dir + today
    f = zipfile.ZipFile(tar_dir, 'w', zipfile.ZIP_DEFLATED, False)
    f.write(def_dir + "R1104.log.txt")
    f.close()
    print 'Successful backup to [%s]' % tar_dir
    print '---end backup---'

if __name__ == '__main__':
    backup()
else:
    print 'being imported from another module...'
