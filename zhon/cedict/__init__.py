"""Provides CC-CEDICT Traditional and Simplified character constants."""

from __future__ import unicode_literals

from . import simplified
from . import traditional

#: A string containing all Simplified characters according to CC-CEDICT.
simp = simplified = simplified.CHARACTERS

#: A string containing all Traditional characters according to CC-CEDICT.
trad = traditional = traditional.CHARACTERS
