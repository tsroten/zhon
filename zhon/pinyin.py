"""RE pattern objects for detecting and splitting Pinyin."""

from __future__ import unicode_literals


RE_NUMBER = """
    (?:(?:(?:(?:[zcs]h|[gkh])uang) |
    (?:[jqx]iong) |
    (?:[nljqx]iang) |
    (?:(?:[zcs]h?|[dtnlgkhjqxy])uan) |
    (?:(?:[zcs]h|[gkh])uai) |
    (?:(?:[zc]h?|[rdtnlgkhsy])ong) |
    (?:(?:[zcs]h?|[rbpmfdtnlgkhw])eng) |
    (?:(?:[zcs]h?|[rbpmfdtnlgkhwy])ang) |
    (?:[bpmdtnljqxy]ing) |
    (?:[bpmdtnljqx]ia[no]) |
    (?:[nl](?:v|u:|\u00FC)e?) |
    (?:[jqxy]ue) |
    (?:[bpmnljqxy]in) |
    (?:[mdnljqx]iu) |
    (?:[bpmdtnljqx]ie) |
    (?:[dljqx]ia) |
    (?:(?:[zcs]h?|[rdtnlgkhy])un) |
    (?:(?:[zcs]h?|[rdtgkh])ui) |
    (?:(?:[zcs]h?|[rdtnlgkh])uo) |
    (?:(?:[zcs]h|[rgkh])ua) |
    (?:(?:[zcs]h?|[rbpmfdngkhw])en) |
    (?:(?:[zcs]h?|[rbpmfdtnlgkhwy])an) |
    (?:(?:[zcs]h?|[rpmfdtnlgkhy])ou) |
    (?:(?:[zcs]h?|[rbpmdtnlgkhy])ao) |
    (?:(?:[zs]h|[bpmfdtnlgkhwz])ei) |
    (?:(?:[zcs]h?|[bpmdtnlgkhw])ai) |
    (?:(?:[zcs]h?|[rjqxybpmdtnl])i) |
    (?:(?:[zcs]h?|[rwbpmfdtnlgkhjqxwy])u) |
    (?:(?:[zcs]h?|[rmdtnlgkhy])e) |
    (?:[bpmfw]o) |
    (?:(?:[zcs]h|[bpmfdtnlgkhzcswy])a) |
    (?:[ea]ng|[ea]n|ou|ao|[ea]i|[aeo])
    )[0-5]?)"""

RE_ACCENT = """
    (?:\u00B7?(?:(?:[zcs]h|[gkh])u
    [a\u0101\u00E0\u00E1\u01CE]ng) |
    (?:[jqx]i[o\u014D\u00F3\u01D2\u00F2]ng) |
    (?:[nljqx]i[a\u0101\u00E0\u00E1\u01CE]ng) |
    (?:(?:[zcs]h?|[dtnlgkhjqxy])u[a\u0101\u00E0\u00E1\u01CE]n) |
    (?:(?:[zcs]h|[gkh])u[a\u0101\u00E0\u00E1\u01CE]i) |
    (?:(?:[zc]h?|[rdtnlgkhsy])[o\u014D\u00F3\u01D2\u00F2]ng) |
    (?:(?:[zcs]h?|[rbpmfdtnlgkhw])[e\u0113\u00E9\u011B\u00E8]ng) |
    (?:(?:[zcs]h?|[rbpmfdtnlgkhwy])
    [a\u0101\u00E0\u00E1\u01CE]ng) |
    (?:[bpmdtnljqxy][i\u012B\u00ED\u01D0\u00EC]ng) |
    (?:[bpmdtnljqx]i[a\u0101\u00E0\u00E1\u01CE][no])|
    (?:[nl][\u00FC\u01D6\u01D8\u01DA\u01DC])|
    (?:[nl]\u00FC[e\u0113\u00E9\u011B\u00E8]?) |
    (?:[jqxy]u[e\u0113\u00E9\u011B\u00E8]) |
    (?:[bpmnljqxy][i\u012B\u00ED\u01D0\u00EC]n) |
    (?:[mdnljqx]i[u\u016B\u00FA\u01D4\u00F9]) |
    (?:[bpmdtnljqx]i[e\u0113\u00E9\u011B\u00E8]) |
    (?:[dljqx]i[a\u0101\u00E0\u00E1\u01CE]) |
    (?:(?:[zcs]h?|[rdtnlgkhy])[u\u016B\u00FA\u01D4\u00F9]n) |
    (?:(?:[zcs]h?|[rdtgkh])u[i\u012B\u00ED\u01D0\u00EC]) |
    (?:(?:[zcs]h?|[rdtnlgkh])u[o\u014D\u00F3\u01D2\u00F2]) |
    (?:(?:[zcs]h|[rgkh])u[a\u0101\u00E0\u00E1\u01CE]) |
    (?:(?:[zcs]h?|[rbpmfdngkhw])[e\u0113\u00E9\u011B\u00E8]n) |
    (?:(?:[zcs]h?|[rbpmfdtnlgkhwy])[a\u0101\u00E0\u00E1\u01CE]n) |
    (?:(?:[zcs]h?|[rpmfdtnlgkhy])[o\u014D\u00F3\u01D2\u00F2]u) |
    (?:(?:[zcs]h?|[rbpmdtnlgkhy])[a\u0101\u00E0\u00E1\u01CE]o) |
    (?:(?:[zs]h|[bpmfdtnlgkhwz])[e\u0113\u00E9\u011B\u00E8]i) |
    (?:(?:[zcs]h?|[bpmdtnlgkhw])[a\u0101\u00E0\u00E1\u01CE]i) |
    (?:(?:[zcs]h?|[rjqxybpmdtnl])[i\u012B\u00ED\u01D0\u00EC]) |
    (?:(?:[zcs]h?|[rwbpmfdtnlgkhjqxwy])
    [u\u016B\u00FA\u01D4\u00F9]) |
    (?:(?:[zcs]h?|[rmdtnlgkhy])[e\u0113\u00E9\u011B\u00E8]) |
    (?:[bpmfw][o\u014D\u00F3\u01D2\u00F2]) |
    (?:(?:[zcs]h?|[bpmfdtnlgkhwy])[a\u0101\u00E0\u00E1\u01CE]) |
    (?:[a\u0101\u00E0\u00E1\u01CE]ng|[e\u0113\u00E9\u011B\u00E8]ng|
    [a\u0101\u00E0\u00E1\u01CE]n|[e\u0113\u00E9\u011B\u00E8]n|
    [o\u014D\u00F3\u01D2\u00F2]u|
    [a\u0101\u00E0\u00E1\u01CE]o|[a\u0101\u00E0\u00E1\u01CE]i|
    [e\u0113\u00E9\u011B\u00E8]i|[a\u0101\u00E0\u00E1\u01CE]|
    [e\u0113\u00E9\u011B\u00E8]|[o\u014D\u00F3\u01D2\u00F2])
    )"""
