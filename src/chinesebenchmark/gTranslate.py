#!/usr/bin/env python
# -*- coding: latin-1 -*-
# orignial code is from
#	https://github.com/mouuff/Google-Translate-API/blob/master/gtranslate.py
# Another implementation is:
#	https://gist.github.com/jseabold/1473363
'''
	Language Code
	-------- ----
	Afrikaans 	af
	Albanian 	sq
	Arabic 	ar
	Belarusian 	be
	Bulgarian 	bg
	Catalan 	ca
	Chinese Simplified 	zh-CN
	Chinese Traditional 	zh-TW
	Croatian 	hr
	Czech 	cs
	Danish 	da
	Dutch 	nl
	English 	en
	Estonian 	et
	Filipino 	tl
	Finnish 	fi
	French 	fr
	Galician 	gl
	German 	de
	Greek 	el
	Hebrew 	iw
	Hindi 	hi
	Hungarian 	hu
	Icelandic 	is
	Indonesian 	id
	Irish 	ga
	Italian 	it
	Japanese 	ja
	Korean 	ko
	Latvian 	lv
	Lithuanian 	lt
	Macedonian 	mk
	Malay 	ms
	Maltese 	mt
	Norwegian 	no
	Persian 	fa
	Polish 	pl
	Portuguese 	pt
	Romanian 	ro
	Russian 	ru
	Serbian 	sr
	Slovak 	sk
	Slovenian 	sl
	Spanish 	es
	Swahili 	sw
	Swedish 	sv
	Thai 	th
	Turkish 	tr
	Ukrainian 	uk
	Vietnamese 	vi
	Welsh 	cy
	Yiddish 	yi
'''
import urllib2

def translate(to_translate, to_langage="auto", langage="auto"):
	'''Return the translation using google translate
	you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?'''
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result

if __name__ == '__main__':
	to_translate = 'How are you?'
	print("%s >> %s" % (to_translate, translate(to_translate)))
	print("%s >> %s" % (to_translate, translate(to_translate, 'zh-CN')))
	#should print Hola como estas >> Hello how are you
	#and Hola como estas? >> Bonjour comment allez-vous?
