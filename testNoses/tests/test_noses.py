#!/usr/bin/env python

from nose.tools import *

def setup():
    print("----------testNotes-----------")
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")
    print("----------testNotes-----------")

def test_basic():
    print("I RAN!")

def test_func():
    print("test function...")

def test_math():
    print("test math 1+1=%d"%(1+1))

