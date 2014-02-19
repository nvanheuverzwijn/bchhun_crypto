#!/usr/bin/python3
import os
import sys
import argparse
import re
import math
import unicodedata

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
		output += unicodedata.category(c) + str(ord(c)*ord(c))
	return output
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="bchhun amazing crypto")
	parser.add_argument("--decode", action="store_true", default=False, help="Decode stuff")
	parser.add_argument("input_string", metavar="STR", nargs="?", default="-", type=str, help="The string to decode or encode. Pass '-' to read from stdin")

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
