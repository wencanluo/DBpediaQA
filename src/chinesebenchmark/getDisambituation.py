# -*- coding: utf-8 -*-  
#!/usr/bin/python

import sys
import codecs
import fio
import json
import chinesebenchmark
import xml.etree.ElementTree as ET
import disambiguate
import slpSRL
    
def getDisambituationWithCorrectNERInput(input, output):
    reload(sys)
    sys.setdefaultencoding('utf8')

    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(input, parser = parser)
    
    root = tree.getroot()
    
    for child in root:
        sentence = ""
        for input in child.findall('NER'):
            if input.attrib['lang'] == 'zh':
                sentence = input.text
                sentence = sentence.replace('&lt;', '<')
                sentence = sentence.replace('&gt;', '>')
                
                data = disambiguate.getNEL(sentence)
                links = disambiguate.extractDisambiguationLink(data)
                
                for k, v in links.items():
                    node = ET.Element(tag='disambiguation', attrib={'lang':'zh', 'entity':k})
                    node.text = v
                    node.tail = '\n'
                    child.insert(0, node)
        
    tree.write(output, encoding = 'utf8')
    
def getDisambituationWithAutomaticNERInput(input, output):
    reload(sys)
    sys.setdefaultencoding('utf8')

    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(input, parser = parser)
    
    root = tree.getroot()
    
    for child in root:
        sentence = ""
        for input in child.findall('string'):
            if input.attrib['lang'] == 'zh':
                sentence = input.text
                sentence = slpSRL.parseNER(sentence)
                data = disambiguate.getNEL(sentence)
                links = disambiguate.extractDisambiguationLink(data)
                
                for k, v in links.items():
                    node = ET.Element(tag='disambiguation', attrib={'lang':'zh', 'entity':k})
                    node.text = v
                    node.tail = '\n'
                    child.insert(0, node)
        
    tree.write(output, encoding = 'utf8')
    
if __name__ == '__main__':
    input = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_linklabel_ner.xml'
    output = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_linklabel_ner_disambigutation.xml'
    output2 = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_linklabel_ner_disambigutation_auto.xml'
    
    #getDisambituationWithCorrectNERInput(input, output)
    getDisambituationWithAutomaticNERInput(input, output2)