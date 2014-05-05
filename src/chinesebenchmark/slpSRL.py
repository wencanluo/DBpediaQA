# -*- coding:utf8 -*-
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

if __name__ == '__main__':
	print getSRL('我是中国人')
