#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Описание всех методов Unittest Framework
"""

import unittest


class TestUnittestMethods(unittest.TestCase):
    def testAssertTrue(self):
        """Вызывает ошибку, если значение аргумента != True"""
        self.assertTrue(True)

    def testFailUnless(self):
        """
            Устаревшее название для assertTrue().
            Вызывает ошибку, если значение аргумента != True
        """
        self.failUnless(True)