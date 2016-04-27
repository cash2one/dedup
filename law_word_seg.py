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
    idx = 0;
    while idx < len(json_data["regulationClause"]):
        wordseg_list = word_seg(json_data["regulationClause"][idx]["clauseBody"].encode('UTF-8', 'ignore'));
        term_list = [i[2] for i in wordseg_list];
        json_data["regulationClause"][idx]["seg"] = term_list
        idx = idx + 1
    print json.dumps(json_data, ensure_ascii=False, sort_keys=True);
