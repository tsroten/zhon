from __future__ import unicode_literals
import re
import unittest
from zhon import jyutping

def is_valid_jyutping(correct_jyutping, s):
    if s in correct_jyutping:
        return True
    return False

def is_valid_jyutping_long(correct_jyutping, ls):
    for w in ls.split(' '):
        if not is_valid_jyutping(correct_jyutping, w):
            return False
    return True


class TestJyutping(unittest.TestCase):

    ts1 = 'deoi4'
    ts2 = 'dop2'
    ts3 = 'ng4'
    ts4 = 'ngo7'
    ts5 = 'ngo5'

    tm1 = 'nei5 hou2'
    tm2 = 'nei2 faalekght33'
    tm3 = 'cin1 keoi3'

    ts6 = 'ng4'

    def test_jyutping_single(self):
        self.assertTrue(is_valid_jyutping(jyutping.correct_jyutping, self.ts1))
        self.assertFalse(is_valid_jyutping(jyutping.correct_jyutping, self.ts2))
        self.assertTrue(is_valid_jyutping(jyutping.correct_jyutping, self.ts3))
        self.assertFalse(is_valid_jyutping(jyutping.correct_jyutping, self.ts4))
        self.assertTrue(is_valid_jyutping(jyutping.correct_jyutping, self.ts5))
        self.assertTrue(is_valid_jyutping(jyutping.correct_jyutping, self.ts6))

    def test_jyutping_multiple(self):
        self.assertTrue(is_valid_jyutping_long(jyutping.correct_jyutping, self.tm1))
        self.assertFalse(is_valid_jyutping_long(jyutping.correct_jyutping, self.tm2))
        self.assertTrue(is_valid_jyutping_long(jyutping.correct_jyutping, self.tm3))
