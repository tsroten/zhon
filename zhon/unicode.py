"""Provides Unicode code point ranges for Chinese text processing constants.

Any constants that have characters with values above 0xFFFF need to be fed
through build_string so as to avoid problems on narrow Python builds.
"""

from __future__ import unicode_literals
import logging
import string
import sys

logger = logging.getLogger(__name__)

chr_func = chr if sys.version_info >= (3, ) else unichr


def build_string(*args):
    """Build a string of code point ranges from a list.

    Takes into account narrow Python builds.

    Parameters:
        one or more lists of ranges or values, e.g.:
            [[0x4E00, 0x9FF],
             [0xF900, 0xFAFF],
             0x20000]

    """
    logger.debug('Building a string from %s args.' % str(len(args)))
    L = []
    for a in args:
        for i in a:
            if isinstance(i, list):
                lower, upper = i
                if lower > sys.maxunicode or upper > sys.maxunicode:
                    logger.debug('Throwing out %s and %s due to '
                                 'narrow Python build.' % (lower, upper))
                    continue
                lower, upper = chr_func(lower), chr_func(upper)
                L.append('%s-%s' % (lower, upper))
            else:
                if i > sys.maxunicode:
                    logger.debug('Throwing out %s due to narrow '
                                 'Python build.' % i)
                    continue
                L.append(chr_func(i))
    return ''.join(L)


HAN_BASE = [[0x4E00, 0x9FFF],  # CJK Unified Ideographs
           [0x3400, 0x4DBF],  # CJK Unified Ideographs Extension A
           [0x20000, 0x2A6DF],  # CJK Unified Ideographs Extension B
           [0x2A700, 0x2B73F],  # CJK Unified Ideographs Extension C
           [0x2B740, 0x2B81F],  # CJK Unified Ideographs Extension D
           [0xF900, 0xFAFF],  # CJK Compatibility Ideographs
           [0x2F800, 0x2FA1F],  # CJK Compatibility Ideographs Supplement
           [0x9FA6, 0x9FCB]]  # Extension to the URO
HAN_IDEOGRAPHS = build_string(HAN_BASE)

RADICALS = ('\u2F00-\u2FD5'  # Kangxi Radicals
            '\u2E80-\u2EF3')  # CJK Radicals Supplement

FULLWIDTH_ALPHANUMERIC = ('\uFF10-\uFF19'  # fullwidth ASCII digits
                          '\uFF21-\uFF3A'  # fullwidth ASCII latin uppercase
                          '\uFF41-\uFF5A')  # fullwidth ASCII latin lowercase

PUNCTUATION = ('\u3001-\u3003'  # comma, full-stop, ditto mark
               '\u3008-\u3011'  # CJK brackets
               '\u3014-\u301F'  # CJK brackets and quotation marks
               '\u3030'  # wavy dash
               '\uFF01-\uFF03'  # fullwidth ASCII variants
               '\uFF05-\uFF0A'  # fullwidth ASCII variants
               '\uFF0C-\uFF0F'  # fullwidth ASCII variants
               '\uFF1A-\uFF1B'  # fullwidth ASCII variants
               '\uFF1F-\uFF20'  # fullwidth ASCII variants
               '\uFF3B-\uFF3D'  # fullwidth brackets
               '\uFF3F'  # fullwidth low line
               '\uFF5B'  # fullwidth curly bracket
               '\uFF5D'  # fullwidth curly bracket
               '\uFF5F-\uFF65'  # fullwidth parens and halfwidth punc.
               '\u2010-\u2015'  # dashes
               '\u201C-\u201D'  # quotation marks
               '\u2026-\u2027'  # elipsis and middle dot
               '\uFE4F'  # wavy underline
               ) + string.punctuation

PINYIN = ('\u003A'  # ascii colon - for the vowel u:
          '\u0031-\u0035'  # ascii numbers 1-5
          '\u0041-\u005A'  # ascii uppercase A-Z
          '\u0061-\u007A'  # ascii lowercase a-z
          '\u00C0-\u00C1'  # upper 4/2 tone A
          '\u00C8-\u00C9'  # upper 4/2 tone E
          '\u00CC-\u00CD'  # upper 4/2 tone I
          '\u00D2-\u00D3'  # upper 4/2 tone O
          '\u00D9-\u00DA'  # upper 4/2 tone U
          '\u00DC'  # upper U:
          '\u00E0-\u00E1'  # lower 4/2 tone a
          '\u00E8-\u00E9'  # lower 4/2 tone e
          '\u00EC-\u00ED'  # lower 4/2 tone i
          '\u00F2-\u00F3'  # lower 4/2 tone o
          '\u00F9-\u00FA'  # lower 4/2 tone u
          '\u00FC'  # lower u:
          '\u0100-\u0103'  # lower and upper 1/3 tone A
          '\u0112-\u0115'  # lower and upper 1/3 tone E
          '\u011A-\u011B'  # lower and upper 3 tone E
          '\u012A-\u012D'  # lower and upper 1/3 tone I
          '\u014C-\u014F'  # lower and upper 1/3 tone O
          '\u016A-\u016D'  # lower and upper 1/3 tone U
          '\u01CD-\u01DC'  # lower/upper A, I, O, U, U:
          ) + string.whitespace

ZHUYIN = ('\u3105-\u312D'  # Bopomofo
          '\u31A0-\u31BA'  # Bopomofo Extended
          '\u02C7'  # caron (3rd tone mark)
          '\u02CA-\u02CB'  # accute and grace accent (2nd and 4th tone marks)
          '\u02D9'  # dot above (5th tone mark)
          ) + string.whitespace
