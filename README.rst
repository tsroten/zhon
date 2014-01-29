Zhon
====

Zhon is a Python library that provides constants commonly used in Chinese text
processing:

* CJK characters and radicals
* Chinese punctuation marks
* Chinese sentence regular expression pattern
* Pinyin vowels, consonants, lowercase, uppercase, and punctuation
* Pinyin syllable, word, and sentence regular expression patterns
* Zhuyin characters and marks
* Zhuyin syllable regular expression pattern
* CC-CEDICT characters

Some quick examples:

* Find CJK characters in a string:

  .. code:: python

    >>> re.findall('[%s]' % zhon.hanzi.characters, 'I broke a plate: 我打破了一个盘子.')
    ['我', '打', '破', '了', '一', '个', '盘', '子']

* Validate Pinyin syllables, words, or sentences:

  .. code:: python

    >>> re.findall(zhon.pinyin.syllable, 'Yuànzi lǐ tíngzhe yí liàng chē.', re.I)
    ['Yuàn', 'zi', 'lǐ', 'tíng', 'zhe', 'yí', 'liàng', 'chē']

    >>> re.findall(zhon.pinyin.word, 'Yuànzi lǐ tíngzhe yí liàng chē.', re.I)
    ['Yuànzi', 'lǐ', 'tíngzhe', 'yí', 'liàng', 'chē']

    >>> re.findall(zhon.pinyin.sentence, 'Yuànzi lǐ tíngzhe yí liàng chē.', re.I)
    ['Yuànzi lǐ tíngzhe yí liàng chē.']

Documentation
-------------

Zhon has `complete documentation <http://zhon.readthedocs.org/en/latest/>`_.
Check it out if you want to find out how to use Zhon.

Name
----

Zhon is short for ZHongwen cONstants. It is pronounced like the name 'John'.

Install
-------

Zhon supports Python 2.7 and 3. Install using pip:

.. code:: bash

    $ pip install zhon


Bugs and Feature Requests
-------------------------

Zhon uses its `GitHub Issues page <https://github.com/tsroten/zhon/issues>`_ 
to track bugs, feature requests, and support questions.

License
-------

Zhon is released under the OSI-approved `MIT License <http://opensource.org/licenses/MIT>`_. See the file LICENSE.txt for more information.
