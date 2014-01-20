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


# This is the end-of-syllable-consonant lookahead assertion.
_NUMBERED_CONSONANT_END = '(?![aeiouv\u00FC]|u:)'

NUMBERED_SYLLABLE = """
    (?:
        (?:(?:[zcs]h|[gkh])uang%(consonant_end)s) |
        (?:[jqx]iong%(consonant_end)s) |
        (?:[nljqx]iang%(consonant_end)s) |
        (?:(?:[zcs]h?|[dtnlgkhrjqxy])uan%(consonant_end)s) |
        (?:(?:[zcs]h|[gkh])uai) |
        (?:(?:[zc]h?|[rdtnlgkhsy])ong%(consonant_end)s) |
        (?:(?:[zcs]h?|[rbpmfdtnlgkhw])?eng%(consonant_end)s) |
        (?:(?:[zcs]h?|[rbpmfdtnlgkhwy])?ang%(consonant_end)s) |
        (?:[bpmdtnljqxy]ing%(consonant_end)s) |
        (?:[bpmdtnljqx]ia(?:o|n%(consonant_end)s)) |
        (?:[nl](?:v|u:|\u00FC)e?) |
        (?:[jqxy]ue) |
        (?:[bpmnljqxy]in%(consonant_end)s) |
        (?:[mdnljqx]iu) |
        (?:[bpmdtnljqx]ie) |
        (?:[dljqx]ia) |
        (?:(?:[zcs]h?|[rdtnlgkhxqjy])un%(consonant_end)s) |
        (?:(?:[zcs]h?|[rdtgkh])ui) |
        (?:(?:[zcs]h?|[rdtnlgkh])uo) |
        (?:(?:[zcs]h|[rgkh])ua) |
        (?:(?:[zcs]h?|[rbpmfdngkhw])?en%(consonant_end)s) |
        (?:(?:[zcs]h?|[rbpmfdtnlgkhwy])?an%(consonant_end)s) |
        (?:(?:[zcs]h?|[rpmfdtnlgkhy])?ou) |
        (?:(?:[zcs]h?|[rbpmdtnlgkhy])?ao) |
        (?:(?:[zs]h|[bpmfdtnlgkhwz])?ei) |
        (?:(?:[zcs]h?|[bpmdtnlgkhw])?ai) |
        (?:(?:[zcs]h?|[rjqxybpmdtnl])i) |
        (?:(?:[zcs]h?|[rwbpmfdtnlgkhjqxwy])u) |
        (?:(?:[zcs]h?|[rmdtnlgkhy])?e) |
        (?:[bpmfwyl]?o) |
        (?:(?:[zcs]h|[bpmfdtnlgkhzcswy])?a)
    )(?:r%(consonant_end)s)?[0-5]?
""" % {'consonant_end': _NUMBERED_CONSONANT_END}

_A = 'a\u0101\u00E0\u00E1\u01CE'
_E = 'e\u0113\u00E9\u011B\u00E8'
_I = 'i\u012B\u00ED\u01D0\u00EC'
_O = 'o\u014D\u00F3\u01D2\u00F2'
_U = 'u\u016B\u00FA\u01D4\u00F9'
_V = 'v\u00FC\u01D6\u01D8\u01DA\u01DC'

# This is the end-of-syllable-consonant lookahead assertion.
_ACCENTED_CONSONANT_END = '(?![%(a)s%(e)s%(i)s%(o)s%(u)s%(v)s]|u:)' % {
    'a': _A, 'e': _E, 'i': _I, 'o': _O, 'u': _U, 'v': _V
}

ACCENTED_SYLLABLE = """
    (?:\u00B7|\u2027)?
    (?:
        (?:(?:[zcs]h|[gkh])u[%(a)s]ng%(consonant_end)s) |
        (?:[jqx]i[%(o)s]ng%(consonant_end)s) |
        (?:[nljqx]i[%(a)s]ng%(consonant_end)s) |
        (?:(?:[zcs]h?|[dtnlgkhrjqxy])u[%(a)s]n%(consonant_end)s) |
        (?:(?:[zcs]h|[gkh])u[%(a)s]i) |
        (?:(?:[zc]h?|[rdtnlgkhsy])[%(o)s]ng%(consonant_end)s) |
        (?:(?:[zcs]h?|[rbpmfdtnlgkhw])?[%(e)s]ng%(consonant_end)s) |
        (?:(?:[zcs]h?|[rbpmfdtnlgkhwy])?[%(a)s]ng%(consonant_end)s) |
        (?:[bpmdtnljqxy][%(i)s]ng%(consonant_end)s) |
        (?:[bpmdtnljqx]i[%(a)s]n%(consonant_end)s) |
        (?:[bpmdtnljqx]i[%(a)s]o) |
        (?:[nl](?:v|u:|\u00FC)[%(e)s]) |
        (?:[nl](?:[%(v)s]|u:)) |
        (?:[jqxy]u[%(e)s]) |
        (?:[bpmnljqxy][%(i)s]n%(consonant_end)s) |
        (?:[mdnljqx]i[%(u)s]) |
        (?:[bpmdtnljqx]i[%(e)s]) |
        (?:[dljqx]i[%(a)s]) |
        (?:(?:[zcs]h?|[rdtnlgkhxqjy])[%(u)s]n%(consonant_end)s) |
        (?:(?:[zcs]h?|[rdtgkh])u[%(i)s]) |
        (?:(?:[zcs]h?|[rdtnlgkh])u[%(o)s]) |
        (?:(?:[zcs]h|[rgkh])u[%(a)s]) |
        (?:(?:[zcs]h?|[rbpmfdngkhw])?[%(e)s]n%(consonant_end)s) |
        (?:(?:[zcs]h?|[rbpmfdtnlgkhwy])?[%(a)s]n%(consonant_end)s) |
        (?:(?:[zcs]h?|[rpmfdtnlgkhy])?[%(o)s]u) |
        (?:(?:[zcs]h?|[rbpmdtnlgkhy])?[%(a)s]o) |
        (?:(?:[zs]h|[bpmfdtnlgkhwz])?[%(e)s]i) |
        (?:(?:[zcs]h?|[bpmdtnlgkhw])?[%(a)s]i) |
        (?:(?:[zcs]h?|[rjqxybpmdtnl])[%(i)s]) |
        (?:(?:[zcs]h?|[rwbpmfdtnlgkhjqxwy])[%(u)s]) |
        (?:(?:[zcs]h?|[rmdtnlgkhy])?[%(e)s]) |
        (?:[bpmfwyl]?[%(o)s]) |
        (?:(?:[zcs]h|[bpmfdtnlgkhzcswy])?[%(a)s])
    )(?:r%(consonant_end)s)?
""" % {
    'consonant_end': _ACCENTED_CONSONANT_END, 'a': _A, 'e': _E, 'i': _I,
    'o': _O, 'u': _U, 'v': _V
}

NUMBERED_WORD = """
    (?:%(ns)s(?:-(?=%(ns)s)|'(?=[aeo])(?=%(ns)s))?[0-9]*)+
""" % {'ns': NUMBERED_SYLLABLE}

ACCENTED_WORD = """
    (?:%(as)s(?:-(?=%(as)s)|'(?=[%(a)s%(e)s%(o)s])(?=%(as)s))?[0-9]*)+
""" % {'as': ACCENTED_SYLLABLE, 'a': _A, 'e': _E, 'o': _O}

N_SYL = NUMBERED_SYL = NUMBERED_SYLLABLE
A_SYL = ACCENTED_SYL = ACCENTED_SYLLABLE
N_WORD = NUMBERED_WORD
A_WORD = ACCENTED_WORD
