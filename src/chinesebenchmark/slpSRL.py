# -*- coding:utf8 -*-
#chinese name entity recognition using http://www.ltp-cloud.com/intro/en/#srl
import urllib2
import json

url_get_base = "http://api.ltp-cloud.com/analysis/?"
api_key = 'h144t7i7MFixIcmauzQh3ETM7iVIpn1BJeOoWN5K'
    
def getSRL(text=''):
    format = 'json'
    pattern = 'srl'
    result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
    #print type(result)
    content = result.read()
    return content

def getNER(text=''):
    #input: a Chinese sentence
    #output: NER result in Json format
    format = 'json'
    pattern = 'ner'
    result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
    #print type(result)
    content = result.read()
    return content

def parseNER(text=''):
    #get the NER result and format it for Agistis
    #input: a Chinese sentence
    content = json.loads(getNER(text), encoding = 'utf-8')
    
    text = []
    for phrase in content[0][0]: #assume the input is only one sentence
        if phrase['ne'] == 'O': #not a NE
            text.append(phrase['cont']) 
        else:
            text.append('<entity>' + phrase['cont'] + '</entity>')
    return " ".join(text)

if __name__ == '__main__':
	#print getNER('我是中国人')
	print parseNER('德国的哪些州是由社會民主黨统治？')
    