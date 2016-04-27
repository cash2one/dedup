#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import sys
import json
hashbits = 64
 #求海明距离
def hamming_distance(sign1, sign2):
    x = (sign1 ^ sign2) & ((1 << hashbits) - 1)
    tot = 0;
    while x :
        tot += 1
        x &= x - 1
    return tot

##1160625178      贵州省人口与计划生育条例        378441742468586926      1160625178,2401340625,3606668028
data = []
idx = 0
for line in sys.stdin:
    token_list = line.strip().split('\t');
    data.append({})
    data[idx]["id"] = token_list[0];
    data[idx]["name"] = token_list[1];
    data[idx]["sign"] = int(token_list[2])
    if len(token_list) == 4:
        data[idx]["seq"] = token_list[3];
    else:
        data[idx]["seq"] = [];
    idx = idx + 1

total_len = len(data)

i = 0;
while i < total_len:
    j = i + 1;
    while j < total_len:
        if data[i]["seq"] != data[j]["seq"]:
            dis = hamming_distance(data[i]["sign"], data[j]["sign"])
            if dis <= 3:
                print json.dumps(data[i], ensure_ascii=False) + "\t" + json.dumps(data[j], ensure_ascii=False) + "\t" + str(dis);
        j = j + 1
    i = i + 1

