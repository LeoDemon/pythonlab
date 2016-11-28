# -*- encoding: utf-8 -*-
#!/usr/bin/env python

from nose.tools import *
from mycla import noseClass

class testCla(object):
    @classmethod
    def setup_class(klass):
        """在实际测试代码运行之前，执行一次函数"""

    @classmethod
    def teardown_class(klass):
        """在实际测试代码运行之后，执行一次"""

    def setup(self):
        """在测试函数运行之前，执行一次"""

    def teardown(self):
        """在测试函数运行之后，执行一次"""

    def test_init(self):
        print("--------test_init---------")
        nc = noseClass()
        assert_equal(nc.value, "Some value")
        assert_not_equal(nc.value, "Incorrect value")

    def test_isOk(self):
        print("--------test_isOk---------")
        nc = noseClass()
        assert_equal(nc.isOk(), True)
        assert_not_equal(nc.isOk(), False)

    def test_raise_exc(self):
        print("--------test_raise_exc---------")
        nc = noseClass()
        assert_raises(KeyError, nc.raise_exc, "A value")

    @raises(KeyError)
    def test_raise_exc_with_decorator(self):
        print("--------test_raise_exc_with_decorator---------")
        nc = noseClass()
        nc.raise_exc("A message")

