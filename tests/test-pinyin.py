# -*- coding: utf-8 -*-
"""Tests for the zhon.pinyin module."""

from __future__ import unicode_literals
import os
import re
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))
from zhon import pinyin

a_re = re.compile(pinyin.RE_ACCENT, re.X | re.I)
n_re = re.compile(pinyin.RE_NUMBER, re.X | re.I)


class TestAccentPinyin(unittest.TestCase):

    def test_all_valid_pinyin(self):
        p = 'Yǒurén diūshīle yī bǎ fǔzi, zěnme zhǎo yě méiyǒu zhǎodào.'
        self.assertEqual(len(''.join(a_re.findall(p))), len(p))

    def test_some_invalid_pinyin(self):
        p = 'Yǒurn diūshle yī bǎ fǔzi, zěnme zhǎo yě méiyǒu zhǎodào.'
        self.assertNotEqual(len(''.join(a_re.findall(p))), len(p))


class TestNumberPinyin(unittest.TestCase):

    def test_all_valid_pinyin(self):
        p = ('You3ren2 diu1shi1le5 yi1 ba3 fu3zi5, zen3me5 zhao3 ye3'
             'mei2you3 zhao3dao4.')
        self.assertEqual(len(''.join(n_re.findall(p))), len(p))

    def test_some_invalid_pinyin(self):
        p = ('Yo3rn2 diu1sh1le5 yi1 ba3 fu3zi5, zen3me5 zhao3 ye3'
             'mei2you3 zhao3dao4.')
        self.assertNotEqual(len(''.join(n_re.findall(p))), len(p))
