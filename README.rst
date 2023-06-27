====
Zhon
====

.. image:: https://badge.fury.io/py/zhon.svg
    :target: https://pypi.org/project/zhon

.. image:: https://github.com/tsroten/zhon/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/tsroten/zhon/actions/workflows/ci.yml

Zhon is a Python library that provides constants commonly used in Chinese text
processing.

* Documentation: https://tsroten.github.io/zhon/
* GitHub: https://github.com/tsroten/zhon
* Support: https://github.com/tsroten/zhon/issues
* Free software: `MIT license <http://opensource.org/licenses/MIT>`_

About
-----

Zhon's constants can be used in Chinese text processing, for example:

* Find CJK characters in a string:

  .. code:: python

    >>> re.findall('[{}]'.format(zhon.hanzi.characters), 'I broke a plate: 我打破了一个盘子.')
    ['我', '打', '破', '了', '一', '个', '盘', '子']

* Validate Pinyin syllables, words, or sentences:

  .. code:: python

    >>> re.findall(zhon.pinyin.syllable, 'Yuànzi lǐ tíngzhe yí liàng chē.', re.I)
    ['Yuàn', 'zi', 'lǐ', 'tíng', 'zhe', 'yí', 'liàng', 'chē']

    >>> re.findall(zhon.pinyin.word, 'Yuànzi lǐ tíngzhe yí liàng chē.', re.I)
    ['Yuànzi', 'lǐ', 'tíngzhe', 'yí', 'liàng', 'chē']

    >>> re.findall(zhon.pinyin.sentence, 'Yuànzi lǐ tíngzhe yí liàng chē.', re.I)
    ['Yuànzi lǐ tíngzhe yí liàng chē.']

Features
--------

Zhon includes the following commonly-used constants:

* CJK characters and radicals
* Chinese punctuation marks
* Chinese sentence regular expression pattern
* Pinyin vowels, consonants, lowercase, uppercase, and punctuation
* Pinyin syllable, word, and sentence regular expression patterns
* Zhuyin characters and marks
* Zhuyin syllable regular expression pattern
* CC-CEDICT characters

Getting Started
---------------

* `Install Zhon <https://tsroten.github.io/zhon/installation.html>`_
* `Learn how to use Zhon <https://tsroten.github.io/zhon/api.html>`_
* `Contribute <https://github.com/tsroten/zhon/blob/develop/CONTRIBUTING.rst>`_ documentation, code, or feedback
