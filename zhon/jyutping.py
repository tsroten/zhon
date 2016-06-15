# -*- coding: utf-8 -*-
"""Constants for processing Jyutping strings."""

from __future__ import unicode_literals
from string import whitespace
import re

tones = ('1', '2', '3', '4', '5', '6')

initials = (
    'b', 'p', 'm', 'f',
    'd', 't', 'n', 'l',
    'j', 'k', 'ng', 'h',
    'gw', 'kw', 'w',
    'z', 'c', 's', 'j'
)

finals = (
    'aa', 'aai', 'aau', 'aam', 'aan', 'aang', 'aap', 'aat', 'aak',
    'ai', 'au', 'am', 'an', 'ang', 'ap', 'at', 'ak',
    'e', 'ei', 'eu', 'em', 'eng', 'ep', 'ek',
    'i', 'iu', 'im', 'in', 'ing', 'ip', 'it', 'ik',
    'o', 'oi', 'ou', 'on', 'ong', 'ot', 'ok',
    'u', 'ui', 'un', 'ung', 'ut', 'uk',
    'oe', 'eoi', 'eon', 'oeng', 'eot', 'eok',
    'yu', 'yun', 'yut'
    'm', 'ng'
)

final_initials = (
    'm', 'ng'
)

reg = ""
for i in initials:
    for f in finals:
        for t in tones:
            reg += "|{0}{1}{2}".format(i, f, t)
for fi in final_initials:
    for t in tones:
        reg += "|{0}{1}{2}".format(fi, "", t)

reg = re.compile(reg.lstrip('|'))
regex = reg
