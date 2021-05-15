# python提取文本的tfidf特征
import csv
import json
import re
from collections import Counter

import requests
from nltk import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

corpus = []

shuju=[]
def read():
    with open("G:/pythonlearn/mykg/utils/text.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        i = 1
        for row in reader:
            #print(i)
            i = i + 1
            tite = row[1]
            comment = row[9]
            new = tite + comment
            corpus.append(new)
            t1 = {}
            t1["Bug_ID"] = row[0]
            t1["product"] = row[2]
            t1["component"] = row[3]
            t1["Type"] = row[4]
            t1["Priority"] = row[5]
            t1["Severity"] = row[6]
            t1["Status"] = row[7]
            t1["Milestone"] = row[8]
            shuju.append(t1)
            # DATAs.objects.create(Bug_ID=row[0],title=row[1],product=row[2],component=row[3],Type=row[4],Priority=row[5],Severity=row[6],Status=row[7],Milestone=row[8],comment=row[9])
        #print(shuju)
        print(len(shuju))


# 去除网址，标点符号，数字等无关信息
def remove(text):
    rep = re.compile(r'http://[a-zA-Z0-9.?/&=:]*', re.S)
    text = rep.sub("", text)
    rep = re.compile(r'https://[a-zA-Z0-9.?/&=:]*', re.S)
    text = rep.sub("", text)
    remove_chars = '[0-9’!"#$%&\'()*+,-./:;<=>?@，>><<。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    return re.sub(remove_chars, '', text)


# corpus = [
#     'Scope of this bug is to add zap style as shown in specs herehttps://www.figma.com/file/KqQZwwLhft9cUIcBtMVmbz/Desktop-First-Run?node-id=45%3A2944This follows pattern from Protocol design system for Mozilla and Firefox websiteshttps://protocol.mozilla.org/patterns/atoms/zap.htmlSee related work by Jgruen on high fidelity prototype using zap:https://firefox-onboard.herokuapp.comhttps://github.com/johngruen/onboarding-appPrototype is built using application framework https://svelte.dev/',
#     '"This was a recent addition to the mock. The middle box now updates when the user changes their resolved breaches on monitor.https://mozilla.invisionapp.com/share/QWWCC2WH7JY#/screens/408637393 Note, also change the \"passwords\" box to match the way the monitor website displays it.',
#     'https://bugzilla.mozilla.org/show_bug.cgi?id=1615060 made changes to remote settings, this is the bug to smoke test those changes before pushing to production Is this good for you? Cheers'
#     'RS client is complaining about Unknown Collection \"main/message-groups\" RemoteSettingsClient.jsm:137. We should create this collection on RS if we wanted to use it, if not, perhaps disable this provider for now.',
# ]
# [输入]:
# 对语料进行分词
word_list = []
import time


headers = {'Content-Type': 'application/json'} ## headers中添加上content-type这个参数，指定为json格式
def fenci():
    for i in range(len(corpus)):
        corpus[i] = remove(corpus[i])

        words = corpus[i].split(' ')  # 按空格分词
        # print(words)
        stops = set(stopwords.words("english"))  # 加载停用词
        cutwords2 = [word.lower() for word in words]  # 全部转化为小写字母
        cutwords3 = [word for word in cutwords2 if word not in stops]
        cutwords4 = [word for word in cutwords3 if 3 < len(word) < 12]
        # lemmatizer = WordNetLemmatizer()
        # tokens = [lemmatizer.lemmatize(word) for word in cutwords4]
        word_list.append(cutwords4)
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

def jisuan():
    for i, count in enumerate(countlist[:]):
        print(i)
        ans = []
        #print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, count, countlist) for word in count}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        #从接口获取数据
        data={}
        an=[]
        data["t"]=corpus[i]
        response = requests.post(url='http://localhost:5006/person/extract', headers=headers,
                                 data=json.dumps(data))  ## post的时候，将data字典形式的参数用json包转换成json格式。
        datas = json.loads(response.text)
        for key in datas:
            if datas[key] != []:
                an = an + datas[key]
        for word, score in sorted_words[:20]:
            ans.append(word)
        answers = list(set(ans+an))
        shuju[i]["describe"]=answers
        print(shuju[i]["describe"])
            #print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
        #print(ans)


if __name__ == '__main__':
    start = time.time()
    read()
    fenci()
    tongji()
    jisuan()
    end = time.time()

    print(str(end - start))

