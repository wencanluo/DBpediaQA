# -*- coding: utf-8 -*-  
#!/usr/bin/python

import sys
import codecs
import fio
import json
import chinesebenchmark
import xml.etree.ElementTree as ET

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
    input = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_zh.xml'
    #output = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_zh_ner.json'
    
    #input = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh.xml'
    #output = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh_ner.json'
    
    output = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_label.xml'
    
    getNELCorrectLabel(input, output)