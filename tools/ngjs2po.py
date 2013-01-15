#!/usr/bin/python

import sys
import demjson

def writePO(fileName, key, obj):
	pluralForms = {'ru-ru': 'nplurals=3; plural=(n % 10 == 1 && n % 100 != 11 ? 0 : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 1 : 2)',
					'en-us': 'nplurals=2; plural=(n != 1)',
					'de-de': 'nplurals=2; plural=(n != 1)',
					'es-es': 'nplurals=2; plural=(n != 1)',
					'ar': 'nplurals=6; plural=n == 0 ? 0 : n == 1 ? 1 : n == 2 ? 2 : n % 100 >= 3 && n % 100 <= 10 ? 3 : n % 100 >= 11 ? 4 : 5'
				}
	poFile = open(opts[1] + key + '.po', 'w')
	poFile.write(u'msgid ""\r\nmsgstr ""\r\n"Plural-Forms: ' + pluralForms[key] + '\\n"\r\n"Content-Type: text/plain; charset=utf-8\\n"\r\n"Content-Transfer-Encoding: 8bit\\n"\r\n');
	for i in obj:
		poFile.write('\r\n')
		poFile.write('msgid "' + i.encode("utf-8") + '"\r\n')
		if isinstance(obj[i], list):
		 	poFile.write('msgid_plural "' + i.encode("utf-8") + '"\r\n')
		 	for k, v in enumerate(obj[i]):
		 		poFile.write('msgstr[' + str(k) + '] "' + v.encode("utf-8") + '"\r\n')
		else:
		 	poFile.write('msgstr "' + obj[i].encode("utf-8") + '"\r\n')
	poFile.close()


opts = sys.argv[1:]
if (len(opts) != 2):
	print 'Both input and output files must be specified'
	sys.exit()

jsonFile = open(opts[0], 'rb')
jsonText = jsonFile.read()
jsonFile.close()

jsonText = jsonText.replace('var _locales = ', '')
jsonText = jsonText.replace('\n', '')

decoded = demjson.decode(jsonText)

for i in decoded:
	writePO(opts[1], i, decoded[i])