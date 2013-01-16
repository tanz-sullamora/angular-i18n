#!/usr/bin/python

import sys
import re
import demjson

def parsePO(locale, poFileName):
	jsonText = "\t\t'" + locale + "': {\n"
	poFile = open(poFileName, 'rb')

	dontForgetToClosePlural = False
	dontForgetToCloseMultiline = False
	passEmptyId = False
	for line in	poFile:
		if ((line == '') or (line == '\n')):
			pass
		else:
			msgid = re.search('msgid "(.*)"', line, re.I | re.S | re.U)
			if msgid:
				if (msgid.group(1) == ''):
					passEmptyId = True
				else:
					passEmptyId = False
					if dontForgetToClosePlural:
						dontForgetToClosePlural = False
						jsonText += '\t\t\t],\n'

					if dontForgetToCloseMultiline:
						dontForgetToCloseMultiline = False
						jsonText += "',\n"

					jsonText += "\t\t\t'" + msgid.group(1) + "': "

			msgidPlural = re.search('msgid_plural "(.+)"', line, re.I | re.S | re.U)
			if msgidPlural:
				jsonText += '[\n'
				dontForgetToClosePlural = True

			if dontForgetToCloseMultiline:
				msgstr = re.search('"(.*)"', line, re.I | re.S | re.U)
				if msgstr:
					jsonText += msgstr.group(1)

			msgstr = re.search('msgstr "(.*)"', line, re.I | re.S | re.U)
			if msgstr:
				if (not passEmptyId):
					if (msgstr.group(1) == ''):
						dontForgetToCloseMultiline = True
						jsonText += "'"
					else:
						jsonText += "'" + msgstr.group(1) + "',\n"

			msgstrPlural = re.search('msgstr\[[0-9]+\] "(.*)"', line, re.I | re.S | re.U)
			if msgstrPlural:
				jsonText += "\t\t\t\t'" + msgstrPlural.group(1) + "',\n"

	poFile.close()

	jsonText += '\t\t},\n\n'

	return jsonText


opts = sys.argv[1:]
if (len(opts) == 0):
	print('Usage:\n  ngpo2js -l ru-ru po1.po -l en-us po2.po -o output.js')
	sys.exit()

locales = {}
for i, v in enumerate(opts):
	if (v == '-o'):
		ouputFileName = opts[i + 1]
	elif (v == '-l'):
		locales[opts[i + 1]] = opts[i + 2]

outputFile = open(ouputFileName, 'wb')
outputFile.write(u'var _locales = {\n')
for i in locales:
	outputFile.write(parsePO(i, locales[i]))
outputFile.write('}')
outputFile.close()