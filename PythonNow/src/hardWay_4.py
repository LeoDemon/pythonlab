#!/usr/bin/env python

# filename: hardWay_4.py
# description: learning python for <<Learn Python the hard way>>
# author: Demon.Lee
# date: 2016.10.31


#Parent class
class P1(object):
    #implicit
    def implicit(self):
        print("P1 implicit()")

    #override
    def override(self):
        print("P1 override()")

    #altered
    def altered(self):
        print("P1 altered()")


#inheritance
class Cp1(P1):
    #override
    def override(self):
        print("Cp1 override()")

    #altered
    def altered(self):
        print("begin...Cp1 altered()")
        super(Cp1, self).altered()
        print("end...Cp1 altered()")


#compose
class Cp2(object):
    #__init__
    def __init__(self):
        self.other = P1()

    #implicit
    def implicit(self):
        self.other.implicit()

    #override
    def override(self):
        print("Cp2 override()")

    #altered
    def altered(self):
        print("begin...Cp2 altered()")
        self.other.altered()
        print("end...Cp2 altered()")


def testEx44():
    print("----------test inheritance---------")
    p1 = P1()
    cp1 = Cp1()
    p1.implicit()
    cp1.implicit()
    p1.override()
    cp1.override()
    p1.altered()
    cp1.altered()
    print("----------test compose---------")
    cp2 = Cp2()
    p1.implicit()
    cp2.implicit()
    p1.override()
    cp2.override()
    p1.altered()
    cp2.altered()

if '__main__' == __name__:
    testEx44()
else:
    print('being imported by another module!')

