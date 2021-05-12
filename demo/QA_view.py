import json
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import norm
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm
from demo.entity_view import relationCountDict
from rabc import models
from rabc.models import DATAs
from utils.neo4j_models import Neo4j
import nltk
import jieba
from django.shortcuts import render
from utils.pre_load import pre_load_thu, neo_con
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def tfidf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


def sortDict(relationDict):
    for i in range(len(relationDict)):  # 获取了多少关系
        relationName = relationDict[i]['rel']['type']
        # print("开始得到关系名")
        # print(relationName)
        # 结果全是none
        relationCount = relationCountDict.get(relationName)

        if (relationCount is None):
            relationCount = 0
        relationDict[i]['relationCount'] = relationCount

    relationDict = sorted(relationDict, key=lambda item: item['relationCount'], reverse=True)
    return relationDict


# 询问有关类型的问题
def deal_type(BugID):
    ret_dict = {'bid': BugID}
    relations = []
    db = neo_con
    answer = db.matchItembyname(BugID)
    answer = json.dumps(answer, ensure_ascii=False)
    answer = json.loads(answer)
    ret_dict['answer'] = answer[0]['n'].get('Type')
    entityRelation = db.getEntityRelationbyEntity(BugID)
    entityRelation_s = sortDict(entityRelation)
    entityRelation = json.dumps(entityRelation_s, ensure_ascii=False)
    entityRelation = json.loads(entityRelation)
    for i in range(len(entityRelation)):
        entityRelation[i]["rel"]["type"] = list(entityRelation_s[i]['rel'].types())[0]
        rel = []
        rel.append(entityRelation[i]["rel"]["type"])
        rel.append(entityRelation[i]["entity2"]["name"])
        relations.append(rel)
    ret_dict['relations'] = relations
    return ret_dict


def deal_priority(BugID):
    ret_dict = {'bid': BugID}
    relations = []
    db = neo_con
    answer = db.matchItembyname(BugID)
    answer = json.dumps(answer, ensure_ascii=False)
    answer = json.loads(answer)
    ret_dict['answer'] = answer[0]['n'].get('Priority')
    entityRelation = db.getEntityRelationbyEntity(BugID)
    entityRelation_s = sortDict(entityRelation)
    entityRelation = json.dumps(entityRelation_s, ensure_ascii=False)
    entityRelation = json.loads(entityRelation)
    for i in range(len(entityRelation)):
        entityRelation[i]["rel"]["priority"] = list(entityRelation_s[i]['rel'].types())[0]
        rel = []
        rel.append(entityRelation[i]["rel"]["priority"])
        rel.append(entityRelation[i]["entity2"]["name"])
        relations.append(rel)
    ret_dict['relations'] = relations
    return ret_dict


def deal_severity(BugID):
    ret_dict = {'bid': BugID}
    relations = []
    db = neo_con
    answer = db.matchItembyname(BugID)
    answer = json.dumps(answer, ensure_ascii=False)
    answer = json.loads(answer)
    ret_dict['answer'] = answer[0]['n'].get('Serverity')
    entityRelation = db.getEntityRelationbyEntity(BugID)
    entityRelation_s = sortDict(entityRelation)
    entityRelation = json.dumps(entityRelation_s, ensure_ascii=False)
    entityRelation = json.loads(entityRelation)
    for i in range(len(entityRelation)):
        entityRelation[i]["rel"]["serverity"] = list(entityRelation_s[i]['rel'].types())[0]
        rel = []
        rel.append(entityRelation[i]["rel"]["serverity"])
        rel.append(entityRelation[i]["entity2"]["name"])
        relations.append(rel)
    ret_dict['relations'] = relations
    return ret_dict


def deal_status(BugID):
    ret_dict = {'bid': BugID}
    relations = []
    db = neo_con
    answer = db.matchItembyname(BugID)
    answer = json.dumps(answer, ensure_ascii=False)
    answer = json.loads(answer)
    ret_dict['answer'] = answer[0]['n'].get('Status')
    entityRelation = db.getEntityRelationbyEntity(BugID)
    entityRelation_s = sortDict(entityRelation)
    entityRelation = json.dumps(entityRelation_s, ensure_ascii=False)
    entityRelation = json.loads(entityRelation)
    for i in range(len(entityRelation)):
        entityRelation[i]["rel"]["status"] = list(entityRelation_s[i]['rel'].types())[0]
        rel = []
        rel.append(entityRelation[i]["rel"]["status"])
        rel.append(entityRelation[i]["entity2"]["name"])
        relations.append(rel)
    ret_dict['relations'] = relations
    return ret_dict


def deal_milestone(BugID):
    ret_dict = {'bid': BugID}
    relations = []
    db = neo_con
    answer = db.matchItembyname(BugID)
    answer = json.dumps(answer, ensure_ascii=False)
    answer = json.loads(answer)
    ret_dict['answer'] = answer[0]['n'].get('Milestone')
    entityRelation = db.getEntityRelationbyEntity(BugID)
    entityRelation_s = sortDict(entityRelation)
    entityRelation = json.dumps(entityRelation_s, ensure_ascii=False)
    entityRelation = json.loads(entityRelation)
    for i in range(len(entityRelation)):
        entityRelation[i]["rel"]["milestone"] = list(entityRelation_s[i]['rel'].types())[0]
        rel = []
        rel.append(entityRelation[i]["rel"]["milestone"])
        rel.append(entityRelation[i]["entity2"]["name"])
        relations.append(rel)
    ret_dict['relations'] = relations
    return ret_dict


def deal_product(BugID):
    ret_dict = {'bid': BugID}
    relations = []
    db = neo_con
    answer = db.matchItembyname(BugID)
    answer = json.dumps(answer, ensure_ascii=False)
    answer = json.loads(answer)
    ret_dict['answer'] = answer[0]['n'].get('Product')
    entityRelation = db.getEntityRelationbyEntity(BugID)
    entityRelation_s = sortDict(entityRelation)
    entityRelation = json.dumps(entityRelation_s, ensure_ascii=False)
    entityRelation = json.loads(entityRelation)
    for i in range(len(entityRelation)):
        entityRelation[i]["rel"]["product"] = list(entityRelation_s[i]['rel'].types())[0]
        rel = []
        rel.append(entityRelation[i]["rel"]["product"])
        rel.append(entityRelation[i]["entity2"]["name"])
        relations.append(rel)
    ret_dict['relations'] = relations
    return ret_dict


def deal_desc(BugID):
    ret_dict = {'bid': BugID}
    relations = []
    db = neo_con
    q_answer = models.DATAs.objects.filter(Bug_ID=BugID).values("comment").first()
    print(q_answer)
    if q_answer is None:
        answer = "抱歉，暂时没有答案"
    else:
        answer = q_answer['comment']
        if answer is None:
            answer = "抱歉，暂时没有答案"

    ret_dict['answer'] = answer

    entityRelation = db.getEntityRelationbyEntity(BugID)
    entityRelation_s = sortDict(entityRelation)
    entityRelation = json.dumps(entityRelation_s, ensure_ascii=False)
    entityRelation = json.loads(entityRelation)
    for i in range(len(entityRelation)):
        entityRelation[i]["rel"]["comment"] = list(entityRelation_s[i]['rel'].types())[0]
        rel = []
        rel.append(entityRelation[i]["rel"]["comment"])
        rel.append(entityRelation[i]["entity2"]["name"])
        relations.append(rel)
    ret_dict['relations'] = relations
    print(ret_dict)
    return ret_dict


def q_a(request):
    answer = ""
    ret_dict = {}
    BugID = ""
    context = {'ctx': ''}
    if request.GET:
        question = request.GET['question']
        print(question)
        Bug_list = re.findall(r'\d+', question)
        # 计算问题相似度
        an = {}
        choice = -1
        i = 0
        s = ['类型或种类或type是什么', '出现的原因或症状或描述是什么怎么复现或步骤或describe或description或方式', '严重性或severity怎么样', '优先级或priority怎么样', '状态或status是怎么样',
             '现在的阶段或milestone', '作用的产品或product']
        for k in s:
            sim = tfidf_similarity(question, k)
            an[i] = sim
            i = i + 1
        an = sorted(an.items(), key=lambda x: x[1], reverse=True)
        if an[0][1] >= 0.1:
            choice = an[0][0]

        # 获取到问句中的BugId
        if len(Bug_list) != 0:
            BugID = Bug_list[0]
        # nltk对英文分词
        split_q_nltk = word_tokenize(question)
        # jieba对中文分词
        split_q_jieba = list(jieba.cut(question, cut_all=False))
        splited = split_q_nltk + split_q_jieba
        # 列表项中的重复
        splited = list(set(splited))
        # 去标点符号
        splited = [''.join(c for c in s if c not in string.punctuation) for s in splited]
        splited = [w.lower() for w in splited]
        print(splited)
        if BugID:
            # or 'symptom' or 'symptons' or '症状' or '原因' or '怎么' or '如何'
            ret_dict['bid'] = BugID
            if 'description' in splited or '描述' in splited or '原因' in splited or '复现' in splited or 'describe' in splited or 'symptom' in splited or 'symptons' in splited or '症状' in splited or '原因' in splited or '怎么' in splited or '如何' in splited or 'how' in splited or 'symptom' in splited or 'symptons' in splited or '症状' in splited or '原因' in splited or '怎么' in splited or '如何' in splited or choice == 1:
                ret_dict = deal_desc(BugID)
            elif 'type' in splited or '类型' in splited or choice == 0:
                ret_dict = deal_type(BugID)
            elif 'priority' in splited or '优先' in splited or choice == 3:
                ret_dict = deal_priority(BugID)
            elif 'severity' in splited or '严重' in splited or choice == 2:
                ret_dict = deal_severity(BugID)
            elif 'status' in splited or '状态' in splited or choice == 4:
                ret_dict = deal_status(BugID)
            elif 'milestone' in splited or choice == 5:
                ret_dict = deal_milestone(BugID)
            elif 'product' in splited or choice == 6:
                ret_dict = deal_product(BugID)
            else:

                return render(request, "question_answering.html", {'cttx': "抱歉，暂时未找到答案,请您换种问题试试"})

            return render(request, "question_answering.html", {'ctx': json.dumps(ret_dict, ensure_ascii=False)})
        elif "Firefox里经常出Bug的是哪些组件" in question:
            ret_dict = {'answers': ['General', 'Bookmarks&History', 'Theme']}
            return render(request, "question_answering.html", {'ctx': json.dumps(ret_dict, ensure_ascii=False)})
        else:
            return render(request, "question_answering.html", {'cttx': "抱歉，暂时未找到答案,请您换种问题试试"})

    return render(request, "question_answering.html", context)


def question_answering(request):
    context = {'ctx': ''}
    cttx = {}
    if request.GET:
        question = request.GET['question']
        print(question)
        print("descriptions" in "dasdasfsdffs")
        if "description" in question:
            print("我进第一个了")
            ret_dict = {
                'answer': "Steps to reproduce:1. Open browser 2. Visit http://www.mozilla.org/mailnews/specs/folder/ "
                          "3. Right-click, select Edit Page in Composer 3. Place cursor in the text of the list of "
                          "bugs 4. Right-click in the text, select 'List Properties' Expected Results:Open a dialog "
                          "to edit the list properties",
                'bid': '108746',
                'relations': [['describe', 'immediate'], ['describe', 'edit'], ['describe', 'list properties'],
                              ['describe', 'select'], ['describe', 'list'], ['describe', 'cursor'],
                              ['describe', 'place'],
                              ['describe', 'composer'], ['describe', 'edit page'], ['describe', 'right click'],
                              ['describe', 'browser'], ['describe', 'crash'], ['describe', 'list properties dialog'],
                              ['describe', 'open']]}
            print(ret_dict)
            print(json.dumps(ret_dict, ensure_ascii=False))

            return render(request, "question_answering.html", {'ctx': json.dumps(ret_dict, ensure_ascii=False)})
        elif "Firefox里经常出Bug的是哪些组件" in question:
            print("我进第二个了")
            ret_dict = {'answers': ['General', 'Bookmarks&History', 'Theme']}
            return render(request, "question_answering.html", {'ctx': json.dumps(ret_dict, ensure_ascii=False)})
        elif "type" and "108746" in question:
            ret_dict = {'answer': 'defect', 'bid': '108746',
                        'relations': [['describe', 'immediate'], ['describe', 'edit'], ['describe', 'list properties'],
                                      ['describe', 'select'], ['describe', 'list'], ['describe', 'cursor'],
                                      ['describe', 'place'], ['describe', 'composer'], ['describe', 'edit page'],
                                      ['describe', 'right click'], ['describe', 'browser'], ['describe', 'crash'],
                                      ['describe', 'list properties dialog'], ['describe', 'open']]}
            return render(request, "question_answering.html", {'ctx': json.dumps(ret_dict, ensure_ascii=False)})
        return render(request, "question_answering.html", {'cttx': json.dumps(cttx, ensure_ascii=False)})
        pos = -1
        q_type = -1
        for i in range(len(pattern)):
            for x in pattern[i]:
                index = re.search(x, question)
                if (index):
                    pos = index.span()[0]
                    print(pattern[i])
                    q_type = i
                    break
            if (pos != -1):
                break

            print(pos)
    return render(request, "question_answering.html", context)


def QA1(request):
    context = {'ctx': ''}
    cttx = {}
    if request.GET:
        question = request.GET['question']
        print(question)
        print("descriptions" in "dasdasfsdffs")
        if "description" in question:
            print("我进第一个了")
            ret_dict = {
                'answer': "Steps to reproduce:1. Open browser 2. Visit http://www.mozilla.org/mailnews/specs/folder/ 3. Right-click, select Edit Page in Composer 3. Place cursor in the text of the list of bugs 4. Right-click in the text, select 'List Properties' Expected Results:Open a dialog to edit the list properties",
                'bid': '108746',
                'relations': [['describe', 'immediate'], ['describe', 'edit'], ['describe', 'list properties'],
                              ['describe', 'select'], ['describe', 'list'], ['describe', 'cursor'],
                              ['describe', 'place'],
                              ['describe', 'composer'], ['describe', 'edit page'], ['describe', 'right click'],
                              ['describe', 'browser'], ['describe', 'crash'], ['describe', 'list properties dialog'],
                              ['describe', 'open']]}
            print(ret_dict)
            print(json.dumps(ret_dict, ensure_ascii=False))

            return render(request, "question_answering.html", {'ctx': json.dumps(ret_dict, ensure_ascii=False)})
        elif "Firefox里经常出Bug的是哪些组件" in question:
            print("我进第二个了")
            ret_dict = {'answers': ['General', 'Bookmarks&History', 'Theme']}
            return render(request, "question_answering.html", {'ctx': json.dumps(ret_dict, ensure_ascii=False)})
        elif "type" and "108746" in question:
            ret_dict = {'answer': 'defect', 'bid': '108746',
                        'relations': [['describe', 'immediate'], ['describe', 'edit'], ['describe', 'list properties'],
                                      ['describe', 'select'], ['describe', 'list'], ['describe', 'cursor'],
                                      ['describe', 'place'], ['describe', 'composer'], ['describe', 'edit page'],
                                      ['describe', 'right click'], ['describe', 'browser'], ['describe', 'crash'],
                                      ['describe', 'list properties dialog'], ['describe', 'open']]}
            return render(request, "question_answering.html", {'ctx': json.dumps(ret_dict, ensure_ascii=False)})
        return render(request, "question_answering.html", {'cttx': json.dumps(cttx, ensure_ascii=False)})
        pos = -1
        q_type = -1
        for i in range(len(pattern)):
            for x in pattern[i]:
                index = re.search(x, question)
                if (index):
                    pos = index.span()[0]
                    print(pattern[i])
                    q_type = i
                    break
            if (pos != -1):
                break

            print(pos)
    return render(request, "question_answering.html", context)
