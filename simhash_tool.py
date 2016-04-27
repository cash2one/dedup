#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json
import hashlib
import random

reload(sys)
sys.setdefaultencoding('utf8')

class Simhash:
    def __init__(self,idf_conf,stopword_conf,hashbit=128):
        self.__hashbit = hashbit
        self.__term_idf = self.__load_idf(idf_conf)
        self.__stopwords = self.__load_stopword(stopword_conf)
    def __utf8_encode(self,string):
        return string.decode('utf8','ignore').encode('utf8','ignore')
    def __string_md5(self,string):
        md5 = hashlib.md5(string).hexdigest()
        return int(md5,16)
    def __load_idf(self,file):
        kv_dict = dict()
        for line in open(file):
            try:
                fields = line.strip().split('\t')
                if len(fields) != 2:
                    continue
                term = fields[0].strip()
                idf = float(fields[1].strip())
                kv_dict[term] = idf
            except:
                continue
        return kv_dict
    def __load_stopword(self,file):
        my_set = set()
        for line in open(file):
            try:
                term = line.strip()
                if len(term) <= 0:
                    continue
                my_set.add(term)
                term = self.__utf8_encode(term)
                my_set.add(term)
            except:
                continue
        return my_set
    def __int2bin(self,value):
        value_bin = bin(value).replace('0b','')
        delta = self.__hashbit - len(value_bin)
        value_bin = '0' * delta + value_bin
        return value_bin
    def simhash_code(self,kv_dict):
        weights = [0] * self.__hashbit
        for k,v in kv_dict.items():
            if k in self.__stopwords or self.__utf8_encode(k) in self.__stopwords:
                continue
            md5 = self.__string_md5(k)
            for i in range(self.__hashbit):
                bitmask = 1 << i
                ret = md5 & bitmask
                if md5 & bitmask:
                    weights[i] += v
                else:
                    weights[i] -= v
        fingerprint = 0
        #print weights
        for i in range(self.__hashbit-1,-1,-1):
            print i;
            if weights[i] >= 0:
                fingerprint += 1 << (self.__hashbit-1-i)
                print 1 << self.__hashbit-1-i;
        #fingerprint = self.__int2bin(fingerprint)
        return fingerprint

def main():
    simhash = Simhash('conf/term.df','conf/stopwords.utf8',64)
    for line in sys.stdin:
        try:
            json_obj = json.loads(line.strip(),encoding='utf8')
            kv_dict = json_obj['keywords']
            title = json_obj['title']
            print kv_dict;
            print title;
            code = simhash.simhash_code(kv_dict)
            print str(code) + '\t' + title
        except Exception,ex:
            continue

if __name__=='__main__':
    main()
