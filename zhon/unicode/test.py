# -*- coding: utf-8 -*-
"""Tests for the zhon.unicode module."""

from __future__ import unicode_literals
import re
import unittest

from zhon import unicode


class TestBuildString(unittest.TestCase):

    def test_range_and_value(self):
        r_v = [[0x50, 0x55], 0x45]
        self.assertEqual(unicode.build_string(r_v), '\u0050-\u0055\u0045')

    def test_value_error(self):
        r_v = [[0x50, 0x55], 0x2000000]
        self.assertEqual(unicode.build_string(r_v), '\u0050-\u0055')

    def test_range_error(self):
        r_v = [[0x50, 0x55], [0x2000000, 0x200000000]]
        self.assertEqual(unicode.build_string(r_v), '\u0050-\u0055')


class TestHanIdeographs(unittest.TestCase):

    def test_all_chinese(self):
        c_re = re.compile('[^%s]' % unicode.HAN_IDEOGRAPHS)
        t = '你我都很她它隹廿'
        self.assertEqual(c_re.search(t), None)

    def test_chinese_and_punc(self):
        c_re = re.compile('[^%s]' % unicode.HAN_IDEOGRAPHS)
        t = '你我都很她它隹廿。，！'
        self.assertNotEqual(c_re.search(t), None)


class TestRadicals(unittest.TestCase):
    pass


class TestFullwidthAlphanumeric(unittest.TestCase):

    def test_all_ascii(self):
        a_re = re.compile('[^%s]' % unicode.FULLWIDTH_ALPHANUMERIC)
        t = '012345678ABCDEabcde'
        self.assertNotEqual(a_re.search(t), None)

    def test_all_fullwidth(self):
        a_re = re.compile('[^%s]' % unicode.FULLWIDTH_ALPHANUMERIC)
        t = '\uFF10\uFF13\uFF22\uFF34\uFF42'
        self.assertEqual(a_re.search(t), None)


class TestPunctuation(unittest.TestCase):
    pass
