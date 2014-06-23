# -*- coding: utf-8 -*-  

#!/usr/bin/python
import httplib, urllib

def getNEL(text = ""):
    # get disambiguation result using Agistis
    # the input is a sentence with name entity result
    params = urllib.urlencode({'type': 'agdistis', 'text': text})
    headers = {}
    conn = httplib.HTTPConnection("127.0.0.1:8080")
    conn.request("POST", "/AGDISTIS", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()

if __name__ == '__main__':
    #input = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_zh.xml'
    #output = '../../benchmark/qald4/qald-4_multilingual_train_withanswers_zh_srl.json'
    
    input = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh.xml'
    output = '../../benchmark/qald4/qald-4_multilingual_test_questions_zh_srl.json'
    getNEL('我 是 <entity>中国</entity> 人')