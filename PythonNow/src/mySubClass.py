
# filename: mySubClass.py
# description: learning class
# author: Demon.Lee
# date: 2016.9.29

from myClass import iClass

class iSubClass(iClass):
    'iSubClass class definition'
    version='0.6'  #class attribute

    def __init__(self, instance_name, key, val, subName):
        print("*************************************")
        iClass.__init__(self, instance_name, key, val)
        self.subName=subName
        self.idoc='learning python inherit class'
        print('sub initializing [%s] instance...'%self.instance_name)

    def displayVersion(self):
        print('sub class version: %s'%iSubClass.version)
        print('sub instance version: %s'%self.version)

    def __del__(self):
        print('sub destructor [%s] iClass'%self.instance_name)

    def showAttr(self):
        print('sub doc: %s'%self.idoc)
        print('sub instance dict: %s'%self.iDict)
        print('sub class dict: %s'%iSubClass.iDict)
        super(iSubClass, self).showAttr()

    @classmethod
    def showAttrParent(cls):
        print('<<<<<<<<<<<<<<<<<<<<<<<')
        super(iSubClass, cls).showAttrPar(cls)
        print('>>>>>>>>>>>>>>>>>>>>>>>')

def testClass():
    ic = iSubClass('ic', 123, 'xyz','subIc')
    ic.displayVersion()    #sub function
    ic.showVersion()    #parent function
    ic.showAttr()
    ic.showAttrParent()
    del ic  #delete the instance
    ic2 = iSubClass('ic2', 378, 'world', 'subIc2')
    ic2.showAttr()


if '__main__' == __name__:
    testClass()
else:
    print('subClass is being imported by another module...')

