Zhon
====

Zhon is a Python module that provides constants commonly used in Chinese text
processing. Current support includes Han characters and radicals, Pinyin, Zhuyin,
and CC-CEDICT characters.

Some simple examples:

* Find Han characters in a string:

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

Overview
--------

Zhon's constants are in one of three formats:

* Character ranges. These are used to build regular expression patterns.
  For example, ``'u\0041-\u005A\u0061-\u007A'``.
* Regular expression pattern. These are regular expression patterns
  that can be used with the regular expression library directly. For
  example, ``'[u\0020-\u007E]+'``.
* Characters listed individually. These can be used with membership tests
  or used to build regular expression patterns. For example, ``'aeiou'``.

``zhon.hanzi.characters``
    This includes character code ranges for all Han ideographs. More
    information is available in
    `Chapter 12 of the Unicode Standard <http://www.unicode.org/versions/Unicode6.0.0/ch12.pdf>`_.
    *Constant format: character ranges*

``zhon.hanzi.radicals``
    This contains the `Kangxi radicals
    <http://www.unicode.org/charts/PDF/U2F00.pdf>`_ and the `CJK Radicals
    Supplement <http://www.unicode.org/charts/PDF/U2E80.pdf>`_. They are used
    in dictionaries to index characters. *Constant format: character ranges.*

``zhon.hanzi.punctuation``
    Character code ranges for Chinese punctuation.
    *Constant format: character ranges*

``zhon.hanzi.sentence``
    A regular expression pattern that matches a Chinese sentence.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.hanzi.sentence, '我买了一辆车。')
        ['我买了一辆车。']

``zhon.pinyin.printable``
    A string that includes every Pinyin printable character or punctuation
    mark (including whitespace). This can be used as a whitelist for Pinyin text.
    *Constant format: characters listed individually*

``zhon.pinyin.syllable`` or ``zhon.pinyin.syl``
    A regular expression pattern that matches a valid Pinyin syllable (accented or
    numbered). Use with the ``re.I`` flag if you want to match uppercase
    letters as well.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.pinyin.syllable, 'Shū zài zhuōzi shàngmian.', re.I)
        ['Shū', 'zài', 'zhuō', 'zi', 'shàng', 'mian']

``zhon.pinyin.accented_syllable``, ``zhon.pinyin.acc_syl``, or ``zhon.pinyin.a_syl``
    A regular expression pattern that matches a valid accented Pinyin syllable.
    Use with the ``re.I`` flag if you want to match uppercase letters as well.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.pinyin.acc_syl, 'Shū zài zhuōzi shàngmian.', re.I)
        ['Shū', 'zài', 'zhuō', 'zi', 'shàng', 'mian']

``zhon.pinyin.numbered_syllable``, ``zhon.pinyin.num_syl``, or ``zhon.pinyin.n_syl``
    A regular expression pattern that matches a valid numbered Pinyin syllable.
    Use with the ``re.I`` flag if you want to match uppercase letters as well.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.pinyin.num_syl, 'Shu1 zai4 zhuo1zi5 shang4mian5.', re.I)
        ['Shu1', 'zai4', 'zhuo1', 'zi5', 'shang4', 'mian5']

``zhon.pinyin.word``
    A regular expression pattern that matches a valid Pinyin word (accented or
    numbered). Use with the ``re.I`` flag if you want to match uppercase
    letters as well.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.pinyin.word, 'Shū zài zhuōzi shàngmian.', re.I)
        ['Shū', 'zài', 'zhuōzi', 'shàngmian']

``zhon.pinyin.accented_word``, ``zhon.pinyin.acc_word``, or ``zhon.pinyin.a_word``
    A regular expression pattern that matches a valid accented Pinyin word.
    Use with the ``re.I`` flag if you want to match uppercase letters as well.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.pinyin.acc_word, 'Shū zài zhuōzi shàngmian.', re.I)
        ['Shū', 'zài', 'zhuōzi', 'shàngmian']

``zhon.pinyin.numbered_word``, ``zhon.pinyin.num_word``, or ``zhon.pinyin.n_word``
    A regular expression pattern that matches a valid numbered Pinyin word.
    Use with the ``re.I`` flag if you want to match uppercase letters as well.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.pinyin.num_word, 'Shu1 zai4 zhuo1zi5 shang4mian5.', re.I)
        ['Shu1', 'zai4', 'zhuo1zi5', 'shang4mian5']

``zhon.pinyin.sentence`` or ``zhon.pinyin.sent``
    A regular expression pattern that matches a valid Pinyin sentence (accented or
    numbered). Use with the ``re.I`` flag if you want to match uppercase
    letters as well.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.pinyin.sentence, 'Shū zài zhuōzi shàngmian.', re.I)
        ['Shū zài zhuōzi shàngmian.']

``zhon.pinyin.accented_sentence``, ``zhon.pinyin.acc_sent``, or ``zhon.pinyin.a_sent``
    A regular expression pattern that matches a valid accented Pinyin sentence.
    Use with the ``re.I`` flag if you want to match uppercase letters as well.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.pinyin.acc_sent, 'Shū zài zhuōzi shàngmian.', re.I)
        ['Shū zài zhuōzi shàngmian.']

``zhon.pinyin.numbered_sentence``, ``zhon.pinyin.num_sent``, or  ``zhon.pinyin.n_sent``
    A regular expression pattern that matches a valid numbered Pinyin sentence.
    Use with the ``re.I`` flag if you want to match uppercase letters as well.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.pinyin.num_sent, 'Shu1 zai4 zhuo1zi5 shang4mian5.', re.I)
        ['Shu1 zai4 zhuo1zi5 shang4mian5.']

``zhon.zhuyin.syllable``
    A regular expression pattern that matches a valid Zhuyin syllable.
    *Constant format: regular expression pattern*

    .. code:: python

        >>> re.findall(zhon.zhuyin.syllable, 'ㄓㄨˋ ㄧㄣ ㄈㄨˊ ㄏㄠˋ')
        ['ㄓㄨˋ', 'ㄧㄣ', 'ㄈㄨˊ', 'ㄏㄠˋ']

``zhon.cedict.traditional``
    A string containing characters considered by CC-CEDICT to be traditional.
    *Constant format: characters listed individually*

``zhon.cedict.simplified``
    A string containing characters considered by CC-CEDICT to be simplified.
    *Constant format: characters listed individually*

Using Zhon's Constants
----------------------

Using the constants listed above is simple. For constants that list the
characters individually, you can perform membership tests or use them in
regular expressions:

.. code:: python

    >>> '车' in zhon.cedict.traditional
    False

    >>> # This regular expression finds all characters that aren't considered
    ... # traditional in CC-CEDICT
    ... re.findall('[^%s]' % zhon.cedict.traditional, '我买了一辆车')
    ['买', '辆', '车']

For constants that contain character code ranges, you'll want to build a
regular expression:

.. code:: python

    >>> re.findall('[%s]' % zhon.hanzi.punctuation, '我买了一辆车。')
    ['。']

For constants that are regular expression patterns, you can use them directly
with the regular expression library, without formatting them:

.. code:: python

    >>> re.findall(zhon.hanzi.sentence, '我买了一辆车。妈妈做的菜，很好吃！')
    ['我买了一辆车。', '妈妈做的菜，很好吃！']

Identifying Text as Chinese
---------------------------

Identifying a character, word, or sentence as Chinese is not a simple
undertaking. Zhon's module hanzi includes Han ideographs, which are not the
same thing as Chinese characters. Chapter 12 of The Unicode Standard has some
useful information about this:

    There is some concern that unifying the Han characters may lead to confusion because they are sometimes used differently by the various East Asian languages. Computationally, Han character unification presents no more difficulty than employing a single Latin character set that is used to write languages as different as English and French. Programmers do not expect the characters "c", "h", "a", and "t" alone to tell us whether chat is a French word for cat or an English word meaning “informal talk.” Likewise, we depend on context to identify the American hood (of a car) with the British bonnet. Few computer users are confused by the fact that ASCII can also be used to represent such words as the Welsh word ynghyd, which are strange looking to English eyes. Although it would be convenient to identify words by language for programs such as spell-checkers, it is neither practical nor productive to encode a separate Latin character set for every language that uses it.

In other words, don't expect Zhon constants to identify a string as Chinese as
opposed to Japanese or Korean. Zhon's ``hanzi.characters`` constant represents all
Han characters, not Chinese characters.

Name
----

Zhon is short for ZHongwen cONstants. It is pronounced like the name 'John'.

Requirements
------------

Zhon supports Python 2.7 and 3.

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
