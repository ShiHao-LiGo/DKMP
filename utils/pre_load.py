# -*- coding: utf-8 -*-

import csv
import sys
import os

import nltk
import thulac
import sys
import csv
import os

sys.path.append("..")

from utils.neo4j_models import Neo4j
# print('thulac open!')
thuFactory = thulac.thulac()
# print('--init thulac()--')
neo_con = Neo4j()  # 预加载neo4j
neo_con.connectDB()
print('neo4j ceonnected!')
pre_load_thu = thulac.thulac()  #默认模式
#
domain_ner_dict = {}
filePath = os.getcwd()
with open(filePath + '/utils/entity_datas.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # 实体 类型代码
        domain_ner_dict[str(row[0]).lower()] = int(row[1])
print('--Load Domain Dictionary...--!')


def get_NE(text):
    # 读取thulac，neo4j，分词
    # db = neo_con
    # 分词
    key_1 = nltk.word_tokenize(text)
    key_1.append('===')  # 末尾加个不合法的，后面好写

    # 读取实体类别,注意要和predict_labels.txt一个目录
    label = domain_ner_dict

    answerList = []
    i = 0
    length = len(key_1) - 1  # 扣掉多加的那个
    while i < length:
        # key_1[i].append(None)
        # key_1[i+1].append(None)
        p1 = key_1[i]
        p2 = key_1[i + 1]
        p12 = p1 + " " + p2
        p1_low = p1.lower()
        p12_low = p12.lower()

        if p12_low in label:  # 组合2个词如果得到实体
            answerList.append([p12, label[p12_low]])
            i += 2
            continue

        if p1_low in label:  # 当前词如果是实体
            answerList.append([p1, label[p1_low]])
            i += 1
            continue

        answerList.append([p1, 0])
        i += 1

    return answerList
