# -*- coding: utf-8 -*-  
#!/usr/bin/python

import sys
import codecs
import fio
import json
import chinesebenchmark
import xml.etree.ElementTree as ET

def getNERformat(sentence, entities):
    prefix = " <entity>"
    posfix = "</entity> "
    
    for entity in entities:
        if sentence.find(entity) == -1:
            print sentence, entities
        sentence = sentence.replace(entity, prefix + entity + posfix)
    
    return sentence
    
def getCorrectNERInput(input, output):
    reload(sys)
    sys.setdefaultencoding('utf8')

    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(input, parser = parser)
    
    root = tree.getroot()
    
    for child in root:
        sentence = ""
        for str in child.findall('string'):
            if str.attrib['lang'] == 'zh':
                sentence = str.text
                
        entities = []
        for link in child.findall('link'):
            if link.attrib['lang'] == 'zh':
                entity = link.attrib['entity']
                entities.append(entity)
                
        sentence = getNERformat(sentence, entities)
        
        node = ET.Element(tag='NER', attrib={'lang':'zh'})
        node.text = sentence
        node.tail = '\n'
        child.insert(0, node)
        
    tree.write(output, encoding = 'utf8')
    
if __name__ == '__main__':
    input = '../../benchmark/qald4/qald-4_multilingual_test_withanswers_linklabel.xml'
    output = '../../benchmark/qald4/qald-4_multilingual_test_withanswers_linklabel_ner.xml'
    
    getCorrectNERInput(input, output)