# filename: myClass.py
# description: learning class for <<Core Python Programming 2nd Edition>> chapter 13
# author: Demon.Lee
# date: 2016.9.29

class iClass(object):
    'iClass class definition'
    iVersion='1.1'  #class attribute
    iCnt=0  #class attribute "recording how many instances have been generated!
    iDict={123:'ott', 188:'yuz'}

    def __init__(self, instance_name, key, val):
        print("------------------------------------")
        iClass.iCnt += 1
        self.iDict[key] = val
        self.idoc='learning python class'
        self.description='learning python class reference content'
        self.func='Test1239'
        self.iVersion='2.0'
        self.instance_name=instance_name
        print('initializing [%s] instance...'%self.instance_name)

    def __del__(self):
        iClass.iCnt -= 1
        print('destructor [%s] iClass'%self.instance_name)

    def showVersion(self):
        print('class version: %s'%iClass.iVersion)
        print('instance version: %s'%self.iVersion)

    def showAttr(self):
        print('current doc: %s'%self.idoc)
        print('current description: %s'%self.description)
        print('current instance dict: %s'%self.iDict)
        print('current class dict: %s'%iClass.iDict)

    def showAttrPar(self):
        print('par instance dict: %s'%self.iDict)
        print('par class dict: %s'%iClass.iDict)

    def showClassCnt(self):
        print('iClass.iCnt: %d'%iClass.iCnt)

    @staticmethod
    def staticFunc():
        print('This is a static method...')

    @classmethod
    def classStaticFunc(cls):
        print('This is a class static method, it is part of class:[%s]...'%cls.__name__)

def testClass():
    ic = iClass('ic', 123, 'xyz')
    ic.showVersion()
    ic.showAttr()
    ic.showClassCnt()  #count class attribute value
    del ic  #delete the instance
    ic2 = iClass('ic2', 378, 'world')
    ic2.showAttr()
    ic3 = iClass('ic3', 1000, 'python')
    ic3.showAttr()
    ic3.showClassCnt()
    print("------------------------------------")
    print("ic2.__dict==%s"%ic2.__dict__)  #instance attribute
    print("iClass.__dict__==%s"%iClass.__dict__)  #class attribute
    print("------------------------------------")
    iClass.staticFunc()
    iClass.classStaticFunc()
    print("------------------------------------")
    ic2.staticFunc()
    ic2.classStaticFunc()
    print("------------------------------------")


#parent class 1                                                #            object
#class P1:                                                     #             /*\
class P1(object):                                              #            /   \
    def showFunc(self):                                        #           /     \
        print("---Hello, This is P111111's showFunc---")       #          /       \
                                                               #         /         \
#parent class 2                                                #        /           \
#class P2:                                                     #        P1          P2
class P2(object):                                              #        | \       / |
    def showFunc(self):                                        #        |  \     /  |
        print("---Hello, This is P222222's showFunc---")       #        |   \   /   |
                                                               #        |    \ /    |
    def testFunc(self):                                        #        |     X     |
        print("---Hello, This is P222222's testFunc---")       #        |    / \    |
                                                               #        |   /   \   |
#child class 1                                                 #        |  /     \  |
class C1(P1,P2):                                               #        C1         C2
    def disFunc(self):                                         #         \         /
        print("---Hello, This is C111111's disFunc---")        #          \       /
                                                               #           \     /
#child class 2                                                 #            \   /
class C2(P1,P2):                                               #             \ /
    def testFunc(self):                                        #              GC
        print("---Hello, This is C222222's testFunc---")

#grandchild class
class GC(C1,C2):
    pass


class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hr, min):
        'Time60 constructor - takes hours and minutes'
        self.hr = hr
        self.min = min

    def __str__(self):
        'Time60 - string representation'
        return '%.2d:%.2d'%(self.hr, self.min)

    __repr__ = __str__

    def __add__(self,other):
        'Time60 - overloading the addition operator'
        new_hr = self.hr+other.hr
        new_min = self.min+other.min
        if(60 <= new_min):
            new_min -= 60
            new_hr += 1
        if(24 <= new_hr):
            new_hr = new_hr - 24
        return self.__class__(new_hr, new_min)

    def __iadd__(self,other):
        'Time60 - overloading the in-place addition operator'
        self.hr=self.hr+other.hr
        self.min=self.min+other.min
        if(60 <= self.min):
            self.min -= 60
            self.hr += 1
        if(24 <= self.hr):
            self.hr= self.hr - 24
        return self

def testTime60():
    mor=Time60(9,36)
    nig=Time60(21,30)
    print("mor==%s"%mor)
    print("nig==", nig)
    print("mor+nig==%s"%(mor+nig))
    mor+=nig
    print("mor==%s"%mor)
    print("mor+nig==%s"%(mor+nig))


class AnyIter(object):
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retVal = []
        for eachItem in range(howmany):
            try:
                retVal.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    print("---safety,return now---")
                    break
                else:
                    print("---howmany==%d, not safe, throw exception now---"%howmany)
                    raise
        return retVal

def testIter():
    aIt = AnyIter(range(10))
    for i in range(1,5):
        print("a%d:%s"%(i,aIt.next(i)))
    print('-----------------')
    bIt = AnyIter(range(10), True)
    for i in range(1,6):
        print("b%d:%s"%(i,bIt.next(i)))


class NumStr(object):
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        return ('[%d::%r]'%(self.__num, self.__string))

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.__num + other.__num, \
                                  self.__string + other.__string)
        else:
            raise TypeError('illegal argument type for built in operation: other is not instance of NumStr')

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.__num * num, \
                                  self.__string * num)
        else:
            raise TypeError('illegal argument type for built in operation: num is not instance of int')

    def __nonzero__(self):
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.__num, other.__num)) + \
            self.__norm_cval(cmp(self.__string, other.__string))

def testNumStr():
    a = NumStr(3, 'aoo')
    b = NumStr(2, 'china')
    # cannot get the __num or __string, because they are private by prefix:'__'
    # print('a.__num==%d'%a.__num)  #you should use a._NumStr__num instead
    print('a.__num==%d'%a._NumStr__num)
    # print('a.__string==%s'%a.__string)
    print('a.__string==%s'%a._NumStr__string)
    print('a==%s'%a)
    print('b==%s'%b)
    print('a*3==%s'%(a*3))
    print('b*2==%s'%(b*2))
    print('a+b==%s'%(a+b))
    print('a>b==%s'%(a>b))
    print('cmp(a,b)==%s'%cmp(a,b))

class A(object):
    def __init__(self):
        print("A __init__")
        #super(A, self).__init__()

class B(object):
    def __init__(self):
        print("B __init__")
        #super(B, self).__init__()

class C(A):
    def __init__(self, arg):
        print("C __init__arg=%s"%arg)
        super(C, self).__init__()

class D(B):
    def __init__(self, arg):
        print("D __init__arg=%s"%arg)
        super(D, self).__init__()

class E(C, D):
    def __init__(self, arg):
        print("E __init__arg=%s"%arg)
        super(E, self).__init__(arg)


#classic classes using depth-first search
#new-style classes using breadth-first search
def testMultiClass():
    gc=GC()
    gc.testFunc()
    gc.showFunc()

    #MRO: Method Resolution Order
    #print(GC.__mro__)
    #print(C1.__mro__)
    #print(C2.__mro__)
    #print(P1.__mro__)

    print('***'*20)
    # GC-MRO:['GC', 'C1', 'C2', 'P1', 'P2', 'object']
    print("GC-MRO:%s"%[x.__name__ for x in GC.__mro__])

#reference url: http://blog.csdn.net/seizef/article/details/5310107
def testMro():
    #E-MRO:['E', 'C', 'A', 'D', 'B', 'object']
    print("E-MRO:%s"%[x.__name__ for x in E.__mro__])
    print('+++'*20)
    e1 = E(10)

if '__main__' == __name__:
    #testClass()
    testMultiClass()
    #testTime60()
    #testIter()
    # testNumStr()
    testMro()
else:
    print('iClass is being imported by another module...')

