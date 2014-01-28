# -*- coding: utf-8 -*-
"""RE pattern objects for detecting and splitting Pinyin.

Splitting pinyin into syllables is not as simple as looking for the maximum
length matches using valid syllables. Instead, lookahead/lookbehind assertions
must be used to validate possible matches. For syllables, the rough approach
used is:
    * Get the longest valid syllable.
    * If it ends in a consonant make sure it's not followed directly by a
        vowel (a hyphen or apostrophe doesn't count).
    * If the above didn't match, repeat for the next longest valid match.

Lookahead/lookbehind assertions are used to ensure that hyphens and
apostrophes are only included in words if used correctly. This helps to weed
out non-Pinyin strings.

"""

from __future__ import unicode_literals
from string import whitespace


vowels = (
    'aɑeiouüvAEIOUÜV'
    'āɑ̄ēīōūǖĀĒĪŌŪǕ'
    'áɑ́éíóúǘÁÉÍÓÚǗ'
    'ǎɑ̌ěǐǒǔǚǍĚǏǑǓǙ'
    'àɑ̀èìòùǜÀÈÌÒÙǛ'
)
consonants = 'bpmfdtnlgkhjqxzcsrzcswyBPMFDTNLGKHJQXZCSRZCSWY'
marks = "·012345:-'"
non_stops = """"#$%&'()*+,-/:;<=>@[\]^_`{|}~"""
stops = '.!?'
punctuation = non_stops + stops
printable = vowels + consonants + marks[:-3] + whitespace + punctuation

_a = 'a\u0101\u00E0\u00E1\u01CE'
_e = 'e\u0113\u00E9\u011B\u00E8'
_i = 'i\u012B\u00ED\u01D0\u00EC'
_o = 'o\u014D\u00F3\u01D2\u00F2'
_u = 'u\u016B\u00FA\u01D4\u00F9'
_v = 'v\u00FC\u01D6\u01D8\u01DA\u01DC'
_a_vowels = {'a': _a, 'e': _e, 'i': _i, 'o': _o, 'u': _u, 'v': _v}
_n_vowels = {'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u', 'v': 'v\u00FC'}


def _build_syl(vowels, tone_numbers=False):
    # This is the end-of-syllable-consonant lookahead assertion.
    consonant_end = '(?![%(a)s%(e)s%(i)s%(o)s%(u)s%(v)s]|u:)' % {
        'a': _a, 'e': _e, 'i': _i, 'o': _o, 'u': _u, 'v': _v
    }
    _vowels = vowels.copy()
    for v, s in _vowels.items():
        if len(s) > 1:
            _vowels[v] = '[%s]' % s
    return (
        '(?:\u00B7|\u2027)?'
        '(?:'
        '(?:(?:[zcs]h|[gkh])u%(a)sng%(consonant_end)s)|'
        '(?:[jqx]i%(o)sng%(consonant_end)s)|'
        '(?:[nljqx]i%(a)sng%(consonant_end)s)|'
        '(?:(?:[zcs]h?|[dtnlgkhrjqxy])u%(a)sn%(consonant_end)s)|'
        '(?:(?:[zcs]h|[gkh])u%(a)si)|'
        '(?:(?:[zc]h?|[rdtnlgkhsy])%(o)sng%(consonant_end)s)|'
        '(?:(?:[zcs]h?|[rbpmfdtnlgkhw])?%(e)sng%(consonant_end)s)|'
        '(?:(?:[zcs]h?|[rbpmfdtnlgkhwy])?%(a)sng%(consonant_end)s)|'
        '(?:[bpmdtnljqxy]%(i)sng%(consonant_end)s)|'
        '(?:[bpmdtnljqx]i%(a)sn%(consonant_end)s)|'
        '(?:[bpmdtnljqx]i%(a)so)|'
        '(?:[nl](?:v|u:|\u00FC)%(e)s)|'
        '(?:[nl](?:%(v)s|u:))|'
        '(?:[jqxy]u%(e)s)|'
        '(?:[bpmnljqxy]%(i)sn%(consonant_end)s)|'
        '(?:[mdnljqx]i%(u)s)|'
        '(?:[bpmdtnljqx]i%(e)s)|'
        '(?:[dljqx]i%(a)s)|'
        '(?:(?:[zcs]h?|[rdtnlgkhxqjy])%(u)sn%(consonant_end)s)|'
        '(?:(?:[zcs]h?|[rdtgkh])u%(i)s)|'
        '(?:(?:[zcs]h?|[rdtnlgkh])u%(o)s)|'
        '(?:(?:[zcs]h|[rgkh])u%(a)s)|'
        '(?:(?:[zcs]h?|[rbpmfdngkhw])?%(e)sn%(consonant_end)s)|'
        '(?:(?:[zcs]h?|[rbpmfdtnlgkhwy])?%(a)sn%(consonant_end)s)|'
        '(?:(?:[zcs]h?|[rpmfdtnlgkhy])?%(o)su)|'
        '(?:(?:[zcs]h?|[rbpmdtnlgkhy])?%(a)so)|'
        '(?:(?:[zs]h|[bpmfdtnlgkhwz])?%(e)si)|'
        '(?:(?:[zcs]h?|[bpmdtnlgkhw])?%(a)si)|'
        '(?:(?:[zcs]h?|[rjqxybpmdtnl])%(i)s)|'
        '(?:(?:[zcs]h?|[rwbpmfdtnlgkhjqxwy])%(u)s)|'
        '(?:(?:[zcs]h?|[rmdtnlgkhy])?%(e)s)|'
        '(?:[bpmfwyl]?%(o)s)|'
        '(?:(?:[zcs]h|[bpmfdtnlgkhzcswy])?%(a)s)'
        ')(?:r%(consonant_end)s)?' + ('[0-5]?' if tone_numbers else '')
    ) % {
        'consonant_end': consonant_end, 'a': _vowels['a'], 'e': _vowels['e'],
        'i': _vowels['i'], 'o': _vowels['o'], 'u': _vowels['u'],
        'v': _vowels['v']
    }


def _build_word(syl, vowels):
    return (
        "(?:%(syl)s(?:-(?=%(syl)s)|'(?=[%(a)s%(e)s%(o)s])(?=%(syl)s))?[0-9]*)+"
    ) % {'syl': syl, 'a': vowels['a'], 'e': vowels['e'], 'o': vowels['o']}


def _build_sentence(word):
    return (
        """(?:%(word)s|[%(non_stops)s\s])+[%(stops)s]['"\]\}\)]*"""
    ) % {'word': word, 'non_stops': non_stops, 'stops': stops}


a_syl = acc_syl = accented_syllable = _build_syl(_a_vowels, tone_numbers=False)
n_syl = num_syl = numbered_syllable = _build_syl(_n_vowels, tone_numbers=True)
syl = syllable = _build_syl(_a_vowels, tone_numbers=True)

a_word = acc_word = accented_word = _build_word(a_syl, _a_vowels)
n_word = num_word = numbered_word = _build_word(n_syl, _n_vowels)
word = _build_word(syl, _a_vowels)

a_sent = acc_sent = accented_sentence = _build_sentence(a_word)
n_sent = num_sent = numbered_sentence = _build_sentence(n_word)
sent = sentence = _build_sentence(word)
