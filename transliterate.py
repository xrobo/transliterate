#!/usr/bin/env python
# -*- coding: utf-8 -*-

def c2l(text):
	ltext = ''
	errors = False
	for c in text.decode("utf-8"):
		if c in chars:
			ltext += chars[c]
	else:
			errors = True
	return ltext, errors

chars = {
    u'а': 'a',
    u'б': 'b',
    u'в': 'v',
    u'г': 'g',
    u'д': 'd',
    u'е': 'e',
    u'ё': 'e',
    u'ж': 'zh',
    u'з': 'z',
    u'и': 'i',
    u'й': 'i',
    u'к': 'k',
    u'л': 'l',
    u'м': 'm',
    u'н': 'n',
    u'о': 'o',
    u'п': 'p',
    u'р': 'r',
    u'с': 's',
    u'т': 't',
    u'у': 'u',
    u'ф': 'f',
    u'х': 'kh',
    u'ц': 'ts',
    u'ч': 'ch',
    u'ш': 'sh',
    u'щ': 'shch',
    u'ъ': 'ie',
    u'ы': 'y',
    u'ь': '',
    u'э': 'e',
    u'ю': 'iu',
    u'я': 'ia',
    u'А': 'A',
    u'Б': 'B',
    u'В': 'V',
    u'Г': 'G',
    u'Д': 'D',
    u'Е': 'E',
    u'Ё': 'E',
    u'Ж': 'Zh',
    u'З': 'Z',
    u'И': 'I',
    u'Й': 'I',
    u'К': 'K',
    u'Л': 'L',
    u'М': 'M',
    u'Н': 'N',
    u'О': 'O',
    u'П': 'P',
    u'Р': 'R',
    u'С': 'S',
    u'Т': 'T',
    u'У': 'U',
    u'Ф': 'F',
    u'Х': 'Kh',
    u'Ц': 'Ts',
    u'Ч': 'Ch',
    u'Ш': 'Sh',
    u'Щ': 'Shch',
    u'Ъ': 'Ie',
    u'Ы': 'Y',
    u'Ь': '',
    u'Э': 'E',
    u'Ю': 'Iu',
    u'Я': 'Ia',
    u' ': ' '
    }
