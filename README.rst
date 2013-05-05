Zhon
====

Zhon is a Python module that provides constants commonly used in Chinese text
processing:

* Chinese characters
* Chinese punctuation
* Pinyin and Zhuyin characters
* Traditional and simplified characters
* ASCII characters
* Fullwidth alphanumeric variants
* Chinese radicals (as used in dictionaries)

Zhon's constants are formatted as strings containing Unicode code ranges. This is
useful for compiling RE pattern objects. They can be combined to
make RE pattern objects as needed.

.. code:: python

    >>> re.findall('[%s]' % zhon.unicode.HAN_IDEOGRAPHS, 'Hello = 你好')
    ['你', '好']

.. code:: python

    >>> re.split('[%s]' % zhon.unicode.PUNCTUATION, '有人丢失了一把斧子，怎么找也没有找到。')
    ['有人丢失了一把斧子', '怎么找也没有找到', '']

.. code:: python

    >>> not_zh_re = re.compile('[^%s%s]' % (zhon.unicode.HAN_IDEOGRAPHS, zhon.unicode.PUNCTUATION))
    >>> not_zh_re.findall('我叫Thomas。你叫什么名字？')
    ['T', 'h', 'o', 'm', 'a', 's']

Overview
--------

zhon.unicode.HAN_IDEOGRAPHS
    This represents every Chinese character (including historic and rare
    characters). HAN_IDEOGRAPHS includes CJK Unified Ideographs, CJK Unified
    Extensions (A-D), CJK Compatibility Ideographs, CJK Compatibility
    Ideographs Supplement, and the extension to the URO. More information is
    available in `Chapter 12 of the Unicode Standard <http://www.unicode.org/versions/Unicode6.0.0/ch12.pdf>`_.

zhon.unicode.PUNCTUATION
    This contains punctuation used in Chinese text.

zhon.unicode.PINYIN
    This contains characters used in Pinyin (both numbered and accented).

zhon.unicode.ZHUYIN
    This contains characters used in Zhuyin (Bopomofo).

zhon.unicode.ASCII
    This contains all ASCII characters.

zhon.unicode.FULLWIDTH_ALPHANUMERIC
    This contains the fullwidth variants for A-Z, a-z, and 0-9.

zhon.unicode.RADICALS
    This contains the `Kangxi radicals
    <http://www.unicode.org/charts/PDF/U2F00.pdf>`_ and the `CJK Radicals
    Supplement <http://www.unicode.org/charts/PDF/U2E80.pdf>`_. They are used
    in dictionaries to index characters.

zhon.cedict.TRADITIONAL
    This contains characters considered by CC-CEDICT to be traditional.

zhon.cedict.SIMPLIFIED
    This contains characters considered by CC-CEDICT to be simplified.

Narrow Python Builds
--------------------

If you have a narrow Python 2 build and run the following code, a ValueError is
raised:

.. code:: python

    >>> unichr(0x20000)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: unichr() arg not in range(0x10000) (narrow Python build)

Narrow Python 3.1/3.2 builds have problems compiling RE pattern objects using
characters ranges greater than 0xFFFF:

.. code:: python

    >>> re.compile('[\U00020000-\U00020005]')
    Traceback (most recent call last):
    ...
    sre_constants.error: bad character range

Narrow Python builds incorrectly handle the character `\U00020000` and others
like it. Zhon takes this into account when building its constants so that you
don't have to worry about it -- characters greater than your Python build's
`sys.maxunicode` are not included in Zhon's constants.

Name
----

Zhon is short for ZHongwen cONstants. It is pronounced like the name 'John'.

Requirements
------------

Zhon supports Python 2.6, 2.7, 3.1, 3.2, and 3.3.

Install
-------

Just use pip:

.. code:: bash

    $ pip install zhon


Bugs/Feature Requests
---------------------

Zhon uses its `GitHub Issues page <https://github.com/tsroten/zhon/issues>`_ to track bugs, feature
requests, and support questions.

License
-------

Zhon is released under the OSI-approved `MIT License <http://opensource.org/licenses/MIT>`_. See the file LICENSE.txt for more information.
