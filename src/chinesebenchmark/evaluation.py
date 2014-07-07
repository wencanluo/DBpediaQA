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
    
def getDisambituationAccuracy(input):
    reload(sys)
    sys.setdefaultencoding('utf8')

    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(input, parser = parser)
    
    root = tree.getroot()
    
    total_count = 0
    empty = 0
    correct_sentence = 0
    
    for child in root:
        total_count = total_count + 1
        dict_disambituation = {}
        for input in child.findall('disambiguation'):
            if input.attrib['lang'] == 'zh':
                entity = input.attrib['entity']
                link = input.text
                dict_disambituation[entity] = link
        
        dict_link = {}
        for input in child.findall('link'):
            if input.attrib['lang'] == 'zh':
                entity = input.attrib['entity']
                link = input.text if input.text != ' ' else None
                dict_link[entity] = link
        
        if len(dict_link) == 0:
            empty = empty + 1
        
        if dict_disambituation == dict_link:
            correct_sentence = correct_sentence + 1
        else:
            print 
            print '*', 
            fio.PrintDict(dict_link)
            print
            print '*',
            fio.PrintDict(dict_disambituation)
            print
    
    print 'Data', '\t', 'N', '\t', 'Correct'#, '\t', 'Empty'
    print 'Train', '\t', total_count,'\t', correct_sentence#, '\t',empty
    
if __name__ == '__main__':
    #input1 = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_linklabel_ner_disambigutation.xml'
    #input2 = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_linklabel_ner_disambigutation_auto.xml'
    
    input1 = '../../benchmark/qald4/qald-4_multilingual_test_withanswers_linklabel_ner_disambigutation2.xml'
    input2 = '../../benchmark/qald4/qald-4_multilingual_test_withanswers_linklabel_ner_disambigutation_auto.xml'
    
    getDisambituationAccuracy(input1)