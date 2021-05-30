#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import sys
import os
import pickle
import time

from scipy.linalg import norm
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def dump():
    corpus = {}
    with open("text2.csv", "r",encoding='utf-8') as f:
        reader = csv.reader(f)
        i = 1
        for row in reader:
            # print(i)
            i = i + 1
            bugid = row[0]
            title = row[1]
            corpus[bugid] = title
    print(corpus)
    # # ------list-> pickle文件---------
    pk_name = open('dit2pic_3000.pk', 'wb')
    pickle.dump(corpus, pk_name)
    pk_name.close()


def read():
    # -------pickle文件->list---------
    pk2_name = open('dit2pic.pk', 'rb')
    list2 = pickle.load(pk2_name)
    # print(list2)
    return list2


def tfidf_similarity(s1, s2):
    def add_space(s):
        return ''.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # print("计算TF-IDF值")
    # print(vectors)
    # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


if __name__ == '__main__':
    dump()
    # 根据具体描述找相似
    # an = {}
    # lists = read()
    # s1 ="Opening link in new tab with Java applet applies that tab's URL, security icon, etc to all tabs"
    # for key, value in lists.items():
    #     sim1 = tfidf_similarity(s1, value)
    #     # sim2 = jaccard_similarity(s1, k)
    #     # sim3=tf_similarity(s3, s1)
    #     an[key] = sim1
    # an = sorted(an.items(), key=lambda x: x[1], reverse=True)
    # print(s1)
    # print(type(an))
    # print(an[:5])
    # 根据ID找相似
    # start = time.time()
    # an = {}
    # lists = read()
    # s1 = "1629951"
    # s1 = lists[s1]
    # # print(s1)
    # for key in lists:
    #     sim1 = tfidf_similarity(s1, lists[key])
    #     # sim2 = jaccard_similarity(s1, k)
    #     # sim3=tf_similarity(s3, s1)
    #     an[key] = sim1
    # an = sorted(an.items(), key=lambda x: x[1], reverse=True)
    # # print(type(an))
    # # print(an[:5])
    # end= time.time()
    # print(end-start)
