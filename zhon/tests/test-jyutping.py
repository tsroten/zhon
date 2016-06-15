from __future__ import unicode_literals
import re
import unittest
from zhon import jyutping

def regex_match(regex, s):
    test = regex.match(s)
    if test is None:
        return 0
    else:
        return 1

class TestJyutping(unittest.TestCase):

    t1 = 'deoi4'
    t2 = 'dop2'
    t3 = 'ng4'
    t4 = 'ngo7'
    t5 = 'ngo5'

    def test_jyutping(self):
        self.assertTrue(regex_match(jyutping.regex, self.t1))
        self.assertFalse(regex_match(jyutping.regex, self.t2))
        self.assertTrue(regex_match(jyutping.regex, self.t3))
        self.assertFalse(regex_match(jyutping.regex, self.t4))
        self.assertTrue(regex_match(jyutping.regex, self.t5))
