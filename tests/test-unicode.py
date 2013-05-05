# -*- coding: utf-8 -*-
"""Tests for the zhon.unicode module."""

from __future__ import unicode_literals
import os
import re
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))
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

    def test_only_radicals(self):
        r_re = re.compile('[^%s]' % unicode.RADICALS)
        t = '\u2F00\u2F31\u2FBA\u2E98\u2EF3\u2ECF'
        self.assertEqual(r_re.search(t), None)

    def test_chinese_equivalents(self):
        r_re = re.compile('[^%s]' % unicode.RADICALS)
        t = '\u4E00\u5E7F\u516B\u5165'
        self.assertNotEqual(r_re.search(t), None)


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

    def test_split_on_punctuation(self):
        p_re = re.compile('[%s]' % unicode.PUNCTUATION)
        t = '你好你好好好哈哈，米饭很好吃；哈哈！'
        self.assertEqual(len(p_re.split(t)), 4)


class TestAscii(unittest.TestCase):

    def test_only_ascii(self):
        a_re = re.compile('[^%s]' % unicode.ASCII)
        t = 'Hello, my name is Zhon.'
        self.assertEqual(a_re.search(t), None)

    def test_ascii_and_chinese(self):
        a_re = re.compile('[^%s]' % unicode.ASCII)
        t = 'Chinese is fun. 中文很有意思。'
        self.assertNotEqual(a_re.search(t), None)
