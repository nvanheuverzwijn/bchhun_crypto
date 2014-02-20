#!/usr/bin/python3.2
import os
import sys
import argparse
import re
import math
import unicodedata
import unittest


def decode(value):
	output = ""
	matches = re.findall("([a-zA-Z]{2})([0-9]+)", value)
	for match in matches:
		unicode_code_point = math.sqrt(float(match[1]))
		output += chr(int(unicode_code_point))
	return output

def encode(value):
	output = ""
	for c in value:
		c2 = ord(c)*ord(c)
		output += unicodedata.category(chr(c2)) + str(c2)
	return output

class QcPyPuzzleTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_encode_email(self):
        self.assertEqual(
            encode("iNfo@quÉbecpythOn.0rg"),
            "So11025Mc6084So10404Nl12321Lo4096So12769Lo13689Lo40401So9604Sm10201So9801Cn12544Lo14641Lo13456Sm10816Lo6241So12100Lo2116Mn2304So12996Sm10609"
        )

    def test_decode_email(self):
        self.assertEqual(
            decode("So11025Mc6084So10404Nl12321Lo4096So12769Lo13689Lo40401So9604Sm10201So9801Cn12544Lo14641Lo13456Sm10816Lo6241So12100Lo2116Mn2304So12996Sm10609"),
            "iNfo@quÉbecpythOn.0rg"
        )


if __name__ == "__main__":
	unittest.main()
	exit()

	parser = argparse.ArgumentParser(description="bchhun's crypto")
	parser.add_argument("--decode", action="store_true", default=False, help="decode STR")
	parser.add_argument("input_string", metavar="STR", type=str, help="the string to decode or encode. Pass '-' to read from stdin.")

	args = parser.parse_args()

	if args.input_string == "-":
		input_string = sys.stdin.readline()
	else:
		input_string = args.input_string

	if args.decode:
		output = decode(input_string)
	else:
		output = encode(input_string)

	print(output)
