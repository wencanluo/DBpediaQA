# -*- coding: utf-8 -*-  
#!/usr/bin/python

import gTranslate, slpSRL
import sys
import codecs
import fio
import json

def getsubstring(s, stag, etag):
    k1 = s.find(stag) + len(stag)
    k2 = s.rfind(etag)
    
    return s[k1:k2]

def translate(input, output):
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    tag1 = '<string lang="en"><![CDATA['
    newtag1 = '<string lang="zh"><![CDATA['
    etag1 = ']]></string>'
    tag2 = '<keywords lang="en"><![CDATA['
    newtag2 = '<keywords lang="zh"><![CDATA['
    etag2 = ']]></keywords>'
    
    SavedStdOut = sys.stdout
    sys.stdout = codecs.open(output, 'wb', 'utf8')
    
    #f = codecs.open("out.txt", 'wb', 'utf8')
    
    #f.write(s.decode('utf8'))
    
    lines = fio.readfile(input)
    
    for line in lines:
        line = line.rstrip()
        
        print line
        
        if line.startswith(tag1):
            s = getsubstring(line,tag1,etag1)
            zhs = gTranslate.translate(s, 'zh-CN')
            print newtag1 + zhs + etag1
        
        if line.startswith(tag2):
            s = getsubstring(line,tag2,etag2)
            zhs = gTranslate.translate(s, 'zh-CN')
            print newtag2 + zhs + etag2
    
    #f.close()
    
    sys.stdout = SavedStdOut

def getSRL(input, output):
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    newtag1 = '<string lang="zh"><![CDATA['
    etag1 = ']]></string>'
    
    lines = fio.readfile(input)
    
    r = []
    
    for line in lines:
        line = line.rstrip()
        
        if line.startswith(newtag1):
            s = getsubstring(line,newtag1,etag1)
            srl = slpSRL.getSRL(s)
            jsrl = json.loads(srl, encoding = 'utf-8')
            r.append(jsrl)
    
    fp = codecs.open(output, 'wb', 'utf8')
    json.dump(r, fp)
    fp.close()
    
def getNER(input, output):
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    newtag1 = '<string lang="zh"><![CDATA['
    etag1 = ']]></string>'
    
    lines = fio.readfile(input)
    
    lr = [] #list for the json result
    
    for line in lines:
        line = line.rstrip()
        
        if line.startswith(newtag1):
            s = getsubstring(line,newtag1,etag1)
            print s
            r = slpSRL.getNER(s)
            jr = json.loads(r, encoding = 'utf-8')
            lr.append(jr)
    
    fp = codecs.open(output, 'wb', 'utf8')
    json.dump(lr, fp)
    fp.close()

if __name__ == '__main__':
    #input = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_zh.xml'
    #output = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_zh_ner.json'
    
    input = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh.xml'
    output = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh_ner.json'
    
    #translate(input, output)
    #getSRL(input, output)
    getNER(input, output)