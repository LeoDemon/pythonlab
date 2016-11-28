# filename: exception.py
# learning try...except...finally

class userExcpetion(Exception):
    '''A user-defined exception class'''
    def __init__(self, errCode, errMsg):
        Exception.__init__(self)
        self.errCode = errCode
        self.errMsg = errMsg

try:
    instr = raw_input('Enter sth::')
    if len(instr) < 3:
        raise userExcpetion('99999', 'the length of input characters was expecting at least 3...')
except EOFError:
    print 'why did you do an EOF on me?'
except userExcpetion, ue:
    print 'userExcpetion:errCode==[%s], errMsg==[%s]' % (ue.errCode, ue.errMsg)
else:
    print 'your input content is [%s]' % instr
finally:
    print 'run over...'
