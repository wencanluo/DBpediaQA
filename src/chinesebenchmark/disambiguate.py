# -*- coding: utf-8 -*-  

#!/usr/bin/python
import httplib, urllib
import sys, json, codecs
import chinesebenchmark
import fio
import slpSRL

def getNEL(text = ""):
    # get disambiguation result using Agistis
    # the input is a sentence with name entity result
    params = urllib.urlencode({'type': 'agdistis', 'text': text})
    headers = {}
    conn = httplib.HTTPConnection("139.18.2.164:8080")
    conn.request("POST", "/AGDISTIS_ZH", params, headers)
    response = conn.getresponse()
    
    try:
        data = response.read()
    except Exception:
        data = None
        print response.status, response.reason
    conn.close()
    return data

def extractDisambiguationLink(data):
    '''extract the dictionary given the data returned by Agistis
    @param data: string
    '''
    links = {}
    
    try:
        data = json.loads(data, encoding = 'utf-8')
        for entity in data:
            name = entity['namedEntity']
            link = entity['disambiguatedURL']
            links[name] = link
    except Exception:
        pass
    
    return links

def getDisambiguate(input, output):
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    lines = fio.readfile(input)
    
    SavedStdOut = sys.stdout
    sys.stdout = codecs.open(output, 'wb', 'utf8')
    
    for line in lines:
        line = line.rstrip()
        s = getNEL(line)
        print s
            
    sys.stdout = SavedStdOut
    
if __name__ == '__main__':
    #input = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_ner.txt'
    #output = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_zh_disambiguation.txt'
    
    #input = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh_ner.txt'
    #output = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh_disambigution.txt'
    
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    data = getNEL('<entity>北京</entity> 是 <entity>中国</entity> 的首都')
    links = extractDisambiguationLink(data)
    print links
    
    #getDisambiguate(input, output)