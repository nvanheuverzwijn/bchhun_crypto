#!/usr/bin/python2.7
#coding: utf-8

import unittest, unicodedata, re, math

class QcPyPuzzleTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_encode_email(self):
        self.assertEqual(
            qcpy_encoder(u"iNfo@quÉbecpythOn.0rg"),
            "So11025Mc6084So10404Nl12321Lo4096So12769Lo13689Lo40401So9604Sm10201So9801Cn12544Lo14641Lo13456Sm10816Lo6241So12100Cn2116Mn2304So12996Sm10609"
        )

    def test_decode_email(self):
        self.assertEqual(
            qcpy_decoder("So11025Mc6084So10404Nl12321Lo4096So12769Lo13689Lo40401So9604Sm10201So9801Cn12544Lo14641Lo13456Sm10816Lo6241So12100Cn2116Mn2304So12996Sm10609"),
            u"iNfo@quÉbecpythOn.0rg".encode("utf-8", "replace")
        )


def qcpy_encoder(decoded):
    encoded = []

    for letter in unicode(decoded):
        number = ord(letter) ** 2
        unic = unichr(number)
        encoded.append(unicodedata.category(unic) + str(number))

    return "".join(encoded)

def qcpy_decoder(encoded):
    decoded = []

    regex = re.compile("\w{2}(\d+)")
    chars = regex.findall(encoded)

    for char in chars:
        new_char_number = int(math.sqrt(float(char)))
        new_char = unichr(new_char_number).encode('utf-8', 'replace')
        decoded.append(new_char)

    return "".join(decoded)

if __name__ == '__main__':
    unittest.main()
