import locale
locale.setlocale(locale.LC_ALL,'en_US.utf8')

from_chars = u'abcdefghijklmnopqrstuvwxyz'
to_chars =   u'\u03b1\u03b2\u03ba\u03b4\u03b5\u03c6\u03b3\u03b7\u03b9\u03be\u03ba\u03bb\u03bc\u03bd\u03bf\u03c0\u03ba\u03c1\u03c3\u03c4\u03c5\u03b2\u03c9\u03c7\u03c5\u03b6'
mymap = {ord(c): ord(t) for c, t in zip(from_chars,to_chars)}

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def basic_rules(st,my_map=mymap):
    s = u'{}'.format(st)
    s = re.sub(r"s$", u'\u03c2', s)
    s = re.sub(r"th$", u'\u03c4\u03b7', s)
    s = s.replace('thn',u'\u03c4\u03b7\u03bd')
    s = s.replace('tha',u'\u03c4\u03b7\u03b1')
    s = s.replace('j',u'\u03c4\u03b6')
    s = s.replace('ha',u'\u03c7\u03b1')
    s = s.replace('b',u'\u03bc\u03c0')
    s = s.replace('ks',u'\u03be')
    s = s.replace('th',u'\u03b8')
    return strip_accents(s.translate(my_map))
