#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import sys;
import re;
import json;
from simhash_demo import *
from my_nlpc_tools import *

def str_to_arr(str):
    return [i.encode('UTF-8', 'ignore') for i in str]

for line in sys.stdin:
    json_data = json.loads(line.strip());

    #regualtionClause = "";
    regualtion_term_list = [];
    for item in json_data["regulationClause"]:
        wordseg_list = word_seg(item["clauseBody"].encode('UTF-8', 'ignore'));
        regualtion_term_list.extend([i[2] for i in wordseg_list]);
        #regualtionClause = regualtionClause + "\n" + item["clauseBody"];
    #regualtion_term_list = str_to_arr(regualtionClause.strip());
    hash_code = Simhash(regualtion_term_list);
    print "\t".join([json_data["@id"], json_data["normalRegulationName"].encode('UTF-8', 'ignore'), str(hash_code), ",".join(json_data["sequenceRegulation"])]);
