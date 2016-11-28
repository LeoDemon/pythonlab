# filename: use_file.py
# writing/reading to/from a file

from operator import add,sub,mul,truediv,mod
from random import randint,choice

ops={'+':add, '-':sub, '*':mul, '/':truediv, '%':mod}
MaxTries=2


def oddChk(num):
    return num%2

def doprob():
    op=choice('+-/*%')
    nums=[randint(1,100) for i in range(3)]
    nums.sort(reverse=True)
    ans=ops[op](nums[0],nums[1])
    if op == '/':
        ans=int(ans)
    prt='%d %s %d = '%(nums[0], op, nums[1])
    oops=0
    while True:
        try:
            if int(input(prt)) == ans:
                print('correct!')
                break
            if oops == MaxTries:
                print('answer\n%s%d'%(prt, ans))
                break
            else:
                print('incorrect...try again...')
                oops+=1
        except (KeyboardInterrupt,EOFError,ValueError):
            print('invalid input...try again...')

def easyMath():
    while True:
        doprob()
        try:
            opt=input('Again?[y or n]:').lower()
            if opt and opt[0] == 'y':
                pass
            else:
                print('choose leaving...')
                break
        except(KeyboardInterrupt, EOFError):
            print('invalid input...leaving...')
            break

def getOdd():
    numList=[]
    for eachNum in range(9):
        numList.append(randint(1,100))
    print('before filter,numList==%s'%numList)
    print('using [oddChk] filter,numList==%s'%list(filter(oddChk, numList)))
    print('using [lambda] filter,numList==%s'%list(filter(lambda n:n%2, numList)))
    print('using [list] filter,numList==%s'%[n for n in numList if n%2])

if __name__ == '__main__':
    getOdd()
else:
    print('...being imported by another module...')

