# -*- coding: utf-8 -*-
"""Constants for working with Chinese characters."""

from __future__ import unicode_literals
import sys

characters = (
    '\u4E00-\u9FFF'  # CJK Unified Ideographs
    '\u3400-\u4DBF'  # CJK Unified Ideographs Extension A
    '\uF900-\uFAFF'  # CJK Compatibility Ideographs
    '\u9FA6-\u9FCB'  # Extension to the URO
)
if sys.maxunicode > 0xFFFF:
    characters += (
        '\U00020000-\U0002A6DF'  # CJK Unified Ideographs Extension B
        '\U0002A700-\U0002B73F'  # CJK Unified Ideographs Extension C
        '\U0002B740-\U0002B81F'  # CJK Unified Ideographs Extension D
        '\U0002F800-\U0002FA1F'  # CJK Compatibility Ideographs Supplement
    )

radicals = (
    '\u2F00-\u2FD5'  # Kangxi Radicals
    '\u2E80-\u2EF3'  # CJK Radicals Supplement
)

non_stops = (
    '\uFF02-\uFF0D'                   # Fullwidth ASCII variants
    '\uFF0F'                          # Fullwidth ASCII variants
    '\uFF1A-\uFF1E'                   # Fullwidth ASCII variants
    '\uFF20'                          # Fullwidth ASCII variants
    '\uFF3B-\uFF40'                   # Fullwidth ASCII variants
    '\uFF5B-\uFF60'                   # Fullwidth ASCII variants
    '\uFF62-\uFF64'                   # Halfwidth CJK punctuation
    '\u3000-\u3001'                   # CJK symbols and punctuation
    '\u3003'                          # CJK symbols and punctutaion
    '\u3008-\u3011'                   # CJK angle and corner brackets
    '\u3014-\u301F'                   # CJK brackets and symbols/punctuation
    '\u3030'                          # Other CJK symbols
    '\u303E-\u303F'                   # Special CJK indicators
    '\u2013-\u2014'                   # Dashes
    '\u2018-\u2019'                   # Quotation marks and apostrophe
    '\u201B-\u201F'                   # Quotation marks and apostrophe
    '\u2026-\u2027'                   # General punctuation
    '\uFE4F'                          # Overscores and underscores
)

stops = (
    '\uFF01'  # Fullwidth exclamation mark
    '\uFF1F'  # Fullwidth question mark
    '\uFF61'  # Halfwidth ideographic full stop
    '\u3002'  # Ideographic full stop
)

punctuation = non_stops + stops

# A sentence end is defined by a stop followed by zero or more
# container-closing marks (e.g. quotation or brackets).
_sentence_end = '[%(stops)s][」﹂”』’》）］｝〕〗〙〛〉】]*' % {'stops': stops}

sentence = '[%(characters)s%(radicals)s%(non_stops)s]*%(sentence_end)s' \
    % {'characters': characters, 'radicals': radicals, 'non_stops': non_stops,
        'sentence_end': _sentence_end}
