# -*- coding: utf-8 -*-  

#!/usr/bin/python

import re
import fio
import os
import sys
import codecs

class MappingTranslator:
    def __init__(self, dataDirectory, inputLangaugeTag="en", outputLangaugeTag="zh"):
        self.inputLangaugeTag = inputLangaugeTag
        self.outputLangaugeTag = outputLangaugeTag
        self.dataDirectory = dataDirectory
        
    def saveMapping(self, name):
        interlanguage_links = self.dataDirectory + "/" + self.inputLangaugeTag + "/interlanguage_links_"+self.inputLangaugeTag+".ttl"
        
        dict = {}
        with open(interlanguage_links, 'r') as f:
            for line in f:
                g = re.search("<http://dbpedia\.org/resource/(.*)>\s*<.*>\s*<http://zh.dbpedia.org/resource/(.*)>\s*.", line)
                if g != None:
                    try:
                        dict[g.group(1)] = g.group(2)
                    except Exception:
                        print line
                        continue
                        
                    
        fio.savePickle(dict, name)
        
    def translateInstanceType(self):
        #read interlanguage_links_en.ttl
        picklename = "en_zh"
        if not os.path.isfile(picklename+'.pickle'):
            self.saveMapping(picklename)
    
        dict = fio.loadPickle(picklename)
        
        # read the instance type
        input = self.dataDirectory + "/" + self.inputLangaugeTag + "/instance_types_"+self.inputLangaugeTag+".ttl"
        output = self.dataDirectory + "/" + self.outputLangaugeTag + "/instance_types_"+self.outputLangaugeTag+".ttl"
        
        SavedStdOut = sys.stdout
        sys.stdout = codecs.open(output, 'wb', 'utf8')
    
        with open(input, 'r') as f:
            for line in f:
                g = re.search("(<http://dbpedia\.org/resource/)(.*)(>\s*<.*>\s*<.*>\s*.)", line)
                if g != None:
                    try:
                        if g.group(2) not in dict: continue
                        print '<http://zh.dbpedia.org/resource/' + dict[g.group(2)] + g.group(3)
                    except Exception:
                        continue
        
        sys.stdout = SavedStdOut
    
    def translateMppingbasedproperties(self):
        #read interlanguage_links_en.ttl
        picklename = "en_zh"
        if not os.path.isfile(picklename+'.pickle'):
            self.saveMapping(picklename)
    
        dict = fio.loadPickle(picklename)
        print len(dict)
        
        # read the instance type
        input = self.dataDirectory + "/" + self.inputLangaugeTag + "/mappingbased_properties_"+self.inputLangaugeTag+".ttl"
        output = self.dataDirectory + "/" + self.outputLangaugeTag + "/mappingbased_properties_"+self.outputLangaugeTag+".ttl"
        
        SavedStdOut = sys.stdout
        sys.stdout = codecs.open(output, 'wb', 'utf8')
    
        with open(input, 'r') as f:
            for line in f:
                g = re.search("(<http://dbpedia\.org/resource/)(.*)(>\s*<.*>\s*<.*>\s*.)", line)
                if g != None:
                    try:
                        if g.group(2) not in dict: continue
                        print '<http://zh.dbpedia.org/resource/' + dict[g.group(2)] + g.group(3)
                    except Exception:
                        continue
        
        sys.stdout = SavedStdOut

    def translateSpecificMappingbasedProperties(self):
        #read interlanguage_links_en.ttl
        picklename = "en_zh"
        if not os.path.isfile(picklename+'.pickle'):
            self.saveMapping(picklename)
    
        dict = fio.loadPickle(picklename)
        print len(dict)
        
        # read the instance type
        input = self.dataDirectory + "/" + self.inputLangaugeTag + "/specific_mappingbased_properties_"+self.inputLangaugeTag+".ttl"
        output = self.dataDirectory + "/" + self.outputLangaugeTag + "/specific_mappingbased_properties_"+self.outputLangaugeTag+".ttl"
        
        SavedStdOut = sys.stdout
        sys.stdout = codecs.open(output, 'wb', 'utf8')
    
        with open(input, 'r') as f:
            for line in f:
                g = re.search("(<http://dbpedia\.org/resource/)(.*)(>\s*<.*>.*<.*>\s*.)", line)
                if g != None:
                    try:
                        if g.group(2) not in dict: continue
                        print '<http://zh.dbpedia.org/resource/' + dict[g.group(2)] + g.group(3)
                    except Exception:
                        continue
        
        sys.stdout = SavedStdOut

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    datadir = '../../../dbpedia3.9'
    
    trans = MappingTranslator(datadir)
    #trans.translateInstanceType()
    #trans.translateMppingbasedproperties()
    trans.translateSpecificMappingbasedProperties()
    
