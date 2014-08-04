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
                        if g.group(1).startswith("Category:"):
                            dict[g.group(1).replace("Category:","")] = g.group(2).replace("Category:","")
                        else:
                            #dict[g.group(1)] = g.group(2)
                            dict[g.group(2)] = g.group(1)
                    except Exception:
                        print line
                        continue
                        
                    
        fio.savePickle(dict, name)
        fio.SaveDict(dict, name + ".txt")
    
    def saveMapping2(self, name):
        interlanguage_links = self.dataDirectory + "/" + self.outputLangaugeTag + "/interlanguage_links_"+self.outputLangaugeTag+".ttl"
        
        dict = {}
        with open(interlanguage_links, 'r') as f:
            for line in f:
                g = re.search("<http://zh.dbpedia\.org/resource/(.*)>\s*<.*>\s*<http://dbpedia.org/resource/(.*)>\s*.", line)
                if g != None:
                    try:
                        dict[g.group(1)] = g.group(2)
                    except Exception:
                        print line
                        continue
                        
                    
        fio.savePickle(dict, name)
        fio.SaveDict(dict, name + ".txt")
        
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
                        #print '<http://dbpedia.org/resource/' + dict[g.group(2)] + g.group(3)
                        print '<http://dbpedia.org/resource/' + g.group(2) + g.group(3)
                    except Exception:
                        continue
        
        sys.stdout = SavedStdOut
    
    def translateLabels1(self):
        # read the instance type
        input = self.dataDirectory + "/" + self.outputLangaugeTag + "/labels_"+self.outputLangaugeTag+".ttl.old"
        output = self.dataDirectory + "/" + self.outputLangaugeTag + "/labels_"+self.outputLangaugeTag+".ttl"
        
        SavedStdOut = sys.stdout
        sys.stdout = codecs.open(output, 'wb', 'utf8')
    
        with open(input, 'r') as f:
            for line in f:
                line = line.strip()
                line = line.replace("zh.dbpedia.org", "dbpedia.org")
                print line
        
        sys.stdout = SavedStdOut
    
    def translateLabels(self):
        
        picklename = "zh_en"
        if not os.path.isfile(picklename+'.pickle'):
            self.saveMapping(picklename)
    
        dict = fio.loadPickle(picklename)
        
        # read the label type
        input = self.dataDirectory + "/" + self.outputLangaugeTag + "/labels_"+self.outputLangaugeTag+".ttl.old"
        output = self.dataDirectory + "/" + self.outputLangaugeTag + "/labels_"+self.outputLangaugeTag+".ttl"
        
        SavedStdOut = sys.stdout
        sys.stdout = codecs.open(output, 'wb', 'utf8')
    
        with open(input, 'r') as f:
            for line in f:
                g = re.search("(<http://zh.dbpedia\.org/resource/)(.*)(>\s*<.*>\s*\")(.*\"@zh\s*.)", line)
                if g != None:
                    try:
                        if g.group(2) not in dict:
                            print '<http://dbpedia.org/resource/' + g.group(2) + g.group(3) + g.group(2) + "\"@zh ."
                        #print '<http://dbpedia.org/resource/' + dict[g.group(2)] + g.group(3) + dict[g.group(2)] + "\"@zh ."
                        else:
                            print '<http://dbpedia.org/resource/' + dict[g.group(2)] + g.group(3) + g.group(2) + "\"@zh ."
                    except Exception:
                        continue
        
        sys.stdout = SavedStdOut
        
    def translateRedirectsTransitive(self):
        # read the instance type
        input = self.dataDirectory + "/" + self.outputLangaugeTag + "/redirects_transitive_"+self.outputLangaugeTag+".ttl.old"
        output = self.dataDirectory + "/" + self.outputLangaugeTag + "/redirects_transitive_"+self.outputLangaugeTag+".ttl"
        
        picklename = "zh_en"
        if not os.path.isfile(picklename+'.pickle'):
            self.saveMapping(picklename)
    
        dict = fio.loadPickle(picklename)
            
        SavedStdOut = sys.stdout
        sys.stdout = codecs.open(output, 'wb', 'utf8')
  
        with open(input, 'r') as f:
            for line in f:
                g = re.search("(<http://zh\.dbpedia\.org/resource/)(.*)(>\s*<)(http://zh\.dbpedia.org/resource/)(.*)(>\s*.)", line)
                if g != None:
                    try:
                        if g.group(5) not in dict:
                            print '<http://dbpedia.org/resource/' + g.group(2) + g.group(3) +"http://dbpedia.org/resource/" + g.group(5) + g.group(6)
                        else:
                            print '<http://dbpedia.org/resource/' + g.group(2) + g.group(3) + "http://dbpedia.org/resource/" + dict[g.group(5)] + g.group(6)  
                    except Exception:
                        continue
        
        sys.stdout = SavedStdOut
    
    def translateRedirectsTransitive2(self):
        # read the instance type
        input = self.dataDirectory + "/" + self.outputLangaugeTag + "/redirects_transitive_"+self.outputLangaugeTag+".ttl.old"
        output = self.dataDirectory + "/" + self.outputLangaugeTag + "/redirects_transitive_"+self.outputLangaugeTag+".ttl"
            
        SavedStdOut = sys.stdout
        sys.stdout = codecs.open(output, 'wb', 'utf8')
  
        with open(input, 'r') as f:
            for line in f:
                line = line.strip()
                line = line.replace("zh.dbpedia.org", "dbpedia.org")
                print line
        
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
                        #print '<http://dbpedia.org/resource/' + dict[g.group(2)] + g.group(3)
                        print '<http://dbpedia.org/resource/' + g.group(2) + g.group(3)
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
                        #print '<http://dbpedia.org/resource/' + dict[g.group(2)] + g.group(3)
                        print '<http://dbpedia.org/resource/' + g.group(2) + g.group(3)
                    except Exception:
                        continue
        
        sys.stdout = SavedStdOut
    
    def translate_raw_infobox_property_definitions(self):
        # read the instance type
        input = self.dataDirectory + "/" + self.outputLangaugeTag + "/raw_infobox_property_definitions_"+self.outputLangaugeTag+".ttl.old"
        output = self.dataDirectory + "/" + self.outputLangaugeTag + "/raw_infobox_property_definitions_"+self.outputLangaugeTag+".ttl"
        
        SavedStdOut = sys.stdout
        sys.stdout = codecs.open(output, 'wb', 'utf8')
    
        with open(input, 'r') as f:
            for line in f:
                line = line.strip()
                line = line.replace("zh.dbpedia.org", "dbpedia.org")
                print line
        
        sys.stdout = SavedStdOut
    
    def extractPropertyNames(self, output):
        # read the label type
        input = self.dataDirectory + "/" + self.outputLangaugeTag + "/raw_infobox_property_definitions_"+self.outputLangaugeTag+".ttl.old"
        
        SavedStdOut = sys.stdout
        sys.stdout = codecs.open(output, 'wb', 'utf8')
        
        dict = {}
        
        with open(input, 'r') as f:
            for line in f:
                g = re.search("<(http://zh.dbpedia\.org/property/.*)>\s*<.*>\s*\"(.*)\"@zh\s*.", line)
                if g != None:
                    try:
                        dict[g.group(2).strip()] = g.group(1).strip()
                    except Exception:
                        continue
        
        sys.stdout = SavedStdOut
        
        fio.SaveDict(dict, self.dataDirectory + "/" + self.outputLangaugeTag + "/" + output + ".txt")
        
if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    datadir = '../../../dbpedia3.9'
    
    trans = MappingTranslator(datadir)
    #trans.saveMapping("en_zh")
    #trans.saveMapping("zh_en")
    #trans.translateInstanceType()
    #trans.translateMppingbasedproperties()
    #trans.translateSpecificMappingbasedProperties()
    #trans.translateLabels()
    #trans.translateRedirectsTransitive()
    #trans.translate_raw_infobox_property_definitions()
    trans.extractPropertyNames("property_names_zh")
    print "Done"
    
