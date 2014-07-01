# -*- coding: utf-8 -*-  
#!/usr/bin/python

import sys
import codecs
import fio
import json
import chinesebenchmark
import xml.etree.ElementTree as ET

def getQuestionKeyword(lines, question):
    k = -1
    for i, line in enumerate(lines):
        line = line.rstrip()
        
        if line == question:
            k = i + 1
            break
    
    if k==-1:
        print line, question
        return None, None
    
    q = None
    keyword = None
    
    i = k
    while i < len(lines):
        line = lines[i].rstrip()
        i = i + 1
        if line.startswith('<string lang="zh"><![CDATA['):
            q = line
            break
    
    i = k
    while i < len(lines):
        line = lines[i].rstrip()
        i = i + 1
        if line.startswith('<keywords lang="zh"><![CDATA['):
            keyword = line
            break
        
    return q, keyword        
    
def CombineTwoXML(input1, input2, output):
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
    
    lines = fio.readfile(input1)
    lines2 = fio.readfile(input2)
    
    M = len(lines)
    kM = 0
    
    for line in lines:
        line = line.rstrip()
        print line
        
        if line.startswith('<question '):
            question = line
            que, keyword = getQuestionKeyword(lines2, line)
        
        if line.startswith(tag1):
            print que
        
        if line.startswith(tag2):
            print keyword
            
    sys.stdout = SavedStdOut

def GetLink(query):
    links = {}
    
    prefix = 'http://dbpedia.org/resource/'
    key = 'res:'
    lines = query.split('\n')
    N = len(lines)
    K = 0
    
    for i in range(N):
        line = lines[i]
        if not line.startswith('WHERE'): 
            continue
        else:
            K = i
            break
    
    for i in range(K, N):
        line = lines[i]
        
        tokens = line.split()
        
        for token in tokens:
            label = token.split(":")
            if len(label)==2:
                if label[0] == 'res':
                    entity = label[1]
                    link = prefix + label[1]
                    links[entity] = link

    return links
    
def getNELCorrectLabel(input, output):
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    picklename = "en_zh"
    dict = fio.loadPickle(picklename)
    
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(input, parser = parser)
    root = tree.getroot()
    
    for child in root:
        print child.tag, child.attrib
#         for str in child.findall('string'):
#             print str.tag, str.attrib, str.text
#         for keywords in child.findall('keywords'):
#             print keywords.tag, keywords.attrib, keywords.text
#         for query in child.findall('query'):
#             print query.text
        for query in child.findall('query'):
#             print query.tex
            links = GetLink(query.text)
            if len(links) > 0:
                for k, v in links.items():
                    node = ET.Element(tag='link', attrib={'lang':'en', 'entity':k})
                    node.text = v
                    node.tail = '\n'
                    child.insert(0, node)
            
            if len(links) > 0:
                for k, v in links.items():
                    if k in dict:
                        k = dict[k]
                        v = 'http://dbpedia.org/resource/' + k
                    else:
                        v = ' '
                    node = ET.Element(tag='link', attrib={'lang':'zh', 'entity':k})
                    node.text = v
                    node.tail = '\n'
                    child.insert(0, node)
            
    tree.write(output, encoding = 'utf8')
    
if __name__ == '__main__':
    #input = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_zh.xml'
    #output = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_zh_ner.json'
    
    #input = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh.xml'
    #output = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh_ner.json'
    
    #output = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_label.xml'
    
    #getNELCorrectLabel(input, output)
    
    #input1 = '../../benchmark/qald4/qald-4_multilingual_test_withanswers.xml'
    #input2 = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh.xml'
    input = '../../benchmark/qald4/qald-4_multilingual_test_withanswers_zh.xml'
    output = '../../benchmark/qald4/qald-4_multilingual_test_withanswers_label.xml'
    #CombineTwoXML(input1, input2, output)
    getNELCorrectLabel(input, output)