#!/usr/bin/env python
"""Identifies input as simplified, traditional, Pinyin, Zhuyin, or ASCII."""
from __future__ import unicode_literals
import argparse
import os
import re
import sys
sys.path.insert(0, os.path.abspath('..'))
import zhon


def parse_args():
    """Parse stdin."""
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='The text you need identified.')
    return parser.parse_args()


def main():
    args = parse_args()

    # compile RE pattern objects
    chinese = re.compile('[^%s%s]' % (zhon.unicode.HAN_IDEOGRAPHS,
                                      zhon.unicode.PUNCTUATION))
    simplified = re.compile('[^%s%s]' % (zhon.cedict.SIMPLIFIED,
                                         zhon.unicode.PUNCTUATION))
    traditional = re.compile('[^%s%s]' % (zhon.cedict.TRADITIONAL,
                                          zhon.unicode.PUNCTUATION))
    pinyin_n = re.compile(zhon.pinyin.RE_NUMBER, re.I | re.X)
    pinyin_a = re.compile(zhon.pinyin.RE_ACCENT, re.I | re.X)
    zhuyin = re.compile('[^%s%s]' % (zhon.unicode.ZHUYIN,
                                     zhon.unicode.PUNCTUATION))
    ascii = re.compile('[^%s]' % zhon.unicode.ASCII)

    # check which pattern object the input matches
    if chinese.search(args.text) is None:
        if (simplified.search(args.text) is None and
                traditional.search(args.text) is None):
            print('Input is simplified or traditional.')
        elif simplified.search(args.text) is None:
            print('Input is simplified.')
        elif traditional.search(args.text) is None:
            print('Input is traditional.')
    elif (len(''.join(pinyin_a.findall(args.text))) == len(args.text) or
          len(''.join(pinyin_n.findall(args.text))) == len(args.text)):
        print('Input is Pinyin.')
    elif zhuyin.search(args.text) is None:
        print('Input is Zhuyin.')
    elif ascii.search(args.text) is None:
        print('Input is ASCII.')
    else:
        print('Input doesn\'t seem to be Chinese, Pinyin, Zhuyin, or ASCII.')


if __name__ == '__main__':
    main()
