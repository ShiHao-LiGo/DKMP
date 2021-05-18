import csv
import json
import os
import re
import time
import pickle
import nltk
import requests
import sys
from py2neo import Graph
# int
from nltk.corpus import stopwords
from collections import Counter
from py2neo import Graph, Node, Relationship

sys.path.append("..")
word_list = []
corpus = []
domain_ner_dict = {}
answers = []


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


# 读取现有语料库
def read():
    # corpus.append(sentence)
    with open("text.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        i = 1
        for row in reader:
            # print(i)
            i = i + 1
            tite = row[1]
            comment = row[9]
            new = tite + comment
            corpus.append(new)
    return corpus


# headers中添加上content-type这个参数，指定为json格式
headers = {'Content-Type': 'application/json'}


# 去除文本中的杂项
def remove(text):
    rep = re.compile(r'http://[a-zA-Z0-9.?/&=:]*', re.S)
    text = rep.sub("", text)
    rep = re.compile(r'https://[a-zA-Z0-9.?/&=:]*', re.S)
    text = rep.sub("", text)
    remove_chars = '[0-9’!"#$%&\'()*+,-./:;<=>?@，>><<。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    return re.sub(remove_chars, '', text)


# text_data = [[1,2,3],[4,5,6]]
# text_txt = 'text.txt'
# with open(text_txt, 'wb') as text:
# 	pickle.dump(text_data, text)

def ReadTxtName():
    lines = []
    with open("G:/pythonlearn/mykg/utils/stop_words.txt", 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    text_txt = 'text.txt'
    with open(text_txt, 'wb') as text:
        pickle.dump(lines, text)


def fenci(sent):
    text_txt = 'text.txt'
    with open(text_txt, 'rb') as text:
        sstop1 = pickle.load(text)
    word_list = kankan()
    # print(sstop1)
    start = time.time()
    # for i in range(len(corpus)):
    sent = remove(sent)

    words = sent.split(' ')  # 按空格分词
    # print(words)
    stops = set(stopwords.words("english"))  # 加载停用词
    cutwords2 = [word.lower() for word in words]  # 全部转化为小写字母
    cutwords3 = [word for word in cutwords2 if word not in stops]
    cutwords4 = [word for word in cutwords3 if 3 < len(word) < 12]
    cutwords4 = [word for word in cutwords4 if word not in sstop1]
    word_list.insert(0, cutwords4)
    # print(word_list)
    return word_list

    # lemmatizer = WordNetLemmatizer()
    # tokens = [lemmatizer.lemmatize(word) for word in cutwords4]

    # print(word_list)


# [输出]:
# [['this', 'is', 'the', 'first', 'document'],
#  ['this', 'is', 'the', 'second', 'second', 'document'],
#  ['and', 'the', 'third', 'one'],
#  ['is', 'this', 'the', 'first', 'document']]
# [输入]:
# 统计词频
countlist = []


def tongji():
    for i in range(len(word_list)):
        count = Counter(word_list[i])
        countlist.append(count)
    return countlist


# [输出]:
# [Counter({'document': 1, 'first': 1, 'is': 1, 'the': 1, 'this': 1}),
#  Counter({'document': 1, 'is': 1, 'second': 2, 'the': 1, 'this': 1}),
#  Counter({'and': 1, 'one': 1, 'the': 1, 'third': 1}),
#  Counter({'document': 1, 'first': 1, 'is': 1, 'the': 1, 'this': 1})]

# word可以通过count得到，count可以通过countlist得到
# 定义计算tfidf公式的函数
# count[word]可以得到每个单词的词频， sum(count.values())得到整个句子的单词总数
def tf(word, count):
    return count[word] / sum(count.values())


# 统计的是含有该单词的句子数
def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)


# len(count_list)是指句子的总数，n_containing(word, count_list)是指含有该单词的句子的总数，加1是为了防止分母为0
def idf(word, count_list):
    return math.log(len(count_list) / (1 + n_containing(word, count_list)))


# 将tf和idf相乘
def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)


# 计算每个单词的tfidf值
import math


def jisuan(sentence):
    for i, count in enumerate(countlist[:2]):
        print(i)
        ans = []
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, count, countlist) for word in count}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        # 从接口获取数据
        data = {}
        an = []
        data["t"] = sentence
        response = requests.post(url='http://localhost:5006/person/extract', headers=headers,
                                 data=json.dumps(data))  ## post的时候，将data字典形式的参数用json包转换成json格式。
        print("1")
        print(response)
        datas = json.loads(response.text)
        print("1")
        print(datas)
        for key in datas:
            if datas[key] != []:
                an = an + datas[key]
        for word, score in sorted_words[:20]:
            ans.append(word)
        filePath = os.getcwd()
        with open('entity_datas.csv', 'r', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                # 实体 类型代码
                domain_ner_dict[str(row[0]).lower()] = int(row[1])
        print('--Load Domain Dictionary...--!')
        # 基于词典来识别实体
        an2 = []
        # 所有字符转化为小写
        key_1 = sentence.casefold()
        # print(key_1)
        key_1 = key_1.split(" ")
        # print(key_1)
        key_1.append(['===', None])
        # print(key_1)
        # print(key_1)
        label = domain_ner_dict  # 实体列表
        pair = []
        NE_list = get_NE(sentence)
        text = ""
        for pair in NE_list:
            if pair[1] == 0:
                text += pair[0] + " "
                continue
            # if pair[0].containsmultiplewords():
            #     text += "["+"<a href=#>" + pair[0] + "</a>" +"]"+" "
            an2.append(pair[0])
            text += "[" + "<a href=#>" + pair[0] + "</a>" + "]" + " "
        # print(text)
        # print(an2)
        answers = list(set(ans + an + an2))
        answers = [word.lower() for word in answers]
        answers = list(set(answers))
        # print(answers)
        return answers
        # print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
        # print(ans)


# 将其他语料预处理好并存起来
def cunchu(words):
    with open('dealed_words', 'wb') as filehandle:
        pickle.dump(words, filehandle)


# 读入存储的预料
def kankan():
    with open('dealed_words', 'rb') as filehandle:
        load_list = pickle.load(filehandle)
    return load_list


def neo4j_build(b_id):
    graph = Graph("http://localhost:7474", username="neo4j", password='123456789')

    node_ID = Node('Bud_Id', name=b_id)
    graph.create(node_ID)

    for k in range(len(answers)):
        t = Node('Describe', name=answers[k])
        graph.create(t)
        relation = Relationship(node_ID, 'Describe', t, name="Describe")
        graph.create(relation)


if __name__ == '__main__':
    # 计算开始的时间
    start = time.time()
    # 加载库中其他缺陷的预处理结果
    load_list = kankan()
    # print(load_list)
    sentence = "Walkthrough has a plan to deploy a new White-Box Testing for Firefox users. We should Smoke Test the UI to reflect this, and migrate Risk from the old endpoint to the new one. Peter, could you please help getting the new endpoint name?"
    # 读取现有语料库
    read()
    # 经过预处理的新数据
    word_list = fenci(sentence)
    # cunchu(word_list)
    tongji()
    # 得到抽取的结果
    answers = jisuan(sentence)
    print(answers)
    # ReadTxtName()
    end = time.time()
    print(str(end - start))
    ts = time.time()
    Bug_Id = str(ts)[0:9]
    print(Bug_Id)
    neo4j_build(Bug_Id)
