__all__ = ['Unicode', 'utf8_unicode_set']

class Unicode:
    MultiByte = int('10000000', 2)
    MultiByte2 = int('11000000', 2)
    MultiByte3 = int('11100000', 2)
    MultiByte4 = int('11110000', 2)
    UC2Val = int('00011111', 2)
    UC3Val = int('00001111', 2)
    UC4Val = int('00000111', 2)
    UCContVal = int('00111111', 2)

    @classmethod
    def from_utf8(cls, utf8char):
        word = 0
        mbytes = utf8char.encode('utf-8')

        byte = mbytes[0]
        if byte < cls.MultiByte:
            word |= byte
        else:
            if byte >= cls.MultiByte4:
                word = byte & cls.UC4Val
            elif byte >= cls.MultiByte3:
                word = byte & cls.UC3Val
            else:
                word = byte & cls.UC2Val

        # copy the last 6 bits of the rest of byte sequence
        for k in range(1, len(mbytes)):
            word <<= 6
            word |= (mbytes[k] & cls.UCContVal)

        return word


def utf8_unicode_set(str, ignore_charset):
    output = set()
    for c in str:
        if c in ignore_charset:
            continue
        unicode = Unicode.from_utf8(c)
        output.add((c,f'U+{hex(unicode)[2:].upper().zfill(4)}'))

    return output
