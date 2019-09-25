__all__ = ['Utf8', 'codepoints_set']

#
#  1. Toy problem came from reading https://www.johndcook.com/blog/2019/09/09/how-utf-8-works/
#  2. Practice/exercise for bitwise operations
#


class Utf8:
    _multibytes = 0x80
    _multibytes_2 = int('11000000', 2)
    _multibytes_3 = int('11100000', 2)
    _multibytes_4 = int('11110000', 2)
    _least_sixbits = int('00111111', 2)
    _mbshift = 6

    def __init__(self, s):
        if isinstance(s, str):
            self._bytes = s.encode('utf-8')
        elif isinstance(s, bytes):
            self._bytes = s
        else:
            raise ValueError('Utf8 expects a string or bytes.')

        self._codepoints = None

    def codepoint(self):
        if self._codepoints:
            return self._codepoints

        iarr = []
        word = 0
        sequence_octets_left = 0

        for b in self._bytes:
            if sequence_octets_left == 0:
                if b & self._multibytes:
                    if b & self._multibytes_4 == self._multibytes_4:
                        word = b ^ self._multibytes_4
                        sequence_octets_left = 3
                    elif b & self._multibytes_3 == self._multibytes_3:
                        word = b ^ self._multibytes_3
                        sequence_octets_left = 2
                    elif b & self._multibytes_2 == self._multibytes_3:
                        word = b ^ self._multibytes_2
                        sequence_octets_left = 1
                    else:
                        raise ValueError('Not a valid utf-8 sequence')
                else:
                    # 00 - 7F
                    word = b
            else:
                if b & self._multibytes == self._multibytes:
                    word <<= self._mbshift
                    word |= (b & self._least_sixbits)
                    sequence_octets_left -= 1
                else:
                    raise ValueError('Not a valid utf-8 sequence')

            if sequence_octets_left == 0:
                iarr.append(word)
                word = 0

        self._codepoints = iarr
        return self._codepoints


def codepoints_set(str, ignore_charset=''):
    output = set()
    for c in str:
        if c in ignore_charset:
            continue
        u = Utf8(c)
        unicode = u.codepoint()[0]
        output.add((c, f'U+{hex(unicode)[2:].upper().zfill(4)}'))

    return output
