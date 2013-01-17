#!/usr/bin/python

import sys
import demjson
import re

def escape(text):
	return text.replace('\\"', '"').replace('"', '\\"')

def writePO(fileName, key, obj):
	pluralForms = {'ru-ru': 'nplurals=3; plural=(n % 10 == 1 && n % 100 != 11 ? 0 : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 1 : 2)',
					'en-us': 'nplurals=2; plural=(n != 1)',
					'de-de': 'nplurals=2; plural=(n != 1)',
					'es-es': 'nplurals=2; plural=(n != 1)',
					'ar': 'nplurals=6; plural=n == 0 ? 0 : n == 1 ? 1 : n == 2 ? 2 : n % 100 >= 3 && n % 100 <= 10 ? 3 : n % 100 >= 11 ? 4 : 5'
				}
	poFile = open(opts[1] + key + '.po', 'w')
	poFile.write(u'msgid ""\nmsgstr ""\n"Plural-Forms: ' + pluralForms[key] + '\\n"\n"Content-Type: text/plain; charset=utf-8\\n"\n"Content-Transfer-Encoding: 8bit\\n"\n');
	for i in obj:
		poFile.write('\n')
		poFile.write('msgid "' + escape(i.encode("utf-8")) + '"\n')
		if isinstance(obj[i], list):
		 	poFile.write('msgid_plural "' + escape(i.encode("utf-8")) + '"\n')
		 	for k, v in enumerate(obj[i]):
		 		poFile.write('msgstr[' + str(k) + '] "' + escape(v.encode("utf-8")) + '"\n')
		else:
		 	poFile.write('msgstr "' + escape(obj[i].encode("utf-8")) + '"\n')
	poFile.close()


opts = sys.argv[1:]
if (len(opts) == 0):
	print('Usage:\n  ngjs2po input.js outputfilename')
	sys.exit()
elif (len(opts) == 1):
	print('Both input and output files must be specified')
	sys.exit()

jsonFile = open(opts[0], 'rb')
jsonText = jsonFile.read()
jsonFile.close()

prefix = re.search('var _locales\s*=\s*({.*})', jsonText, re.I | re.S | re.U)
if (not prefix):
	print('Could not find the "var _locales" definition')
	sys.exit()

decoded = demjson.decode(prefix.group(1))

for i in decoded:
 	writePO(opts[1], i, decoded[i])