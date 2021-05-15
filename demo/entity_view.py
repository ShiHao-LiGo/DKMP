from django.shortcuts import render

# def entity(request):
#     return render(request,"entity.html",None)
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# from toolkit.pre_load import neo_con
from utils.neo4j_models import Neo4j
from utils.pre_load import neo_con
from django.http import JsonResponse
import os
import logging
import json

relationCountDict = {}  # 关系数量的字典
filePath = os.path.abspath(os.path.join(os.getcwd(), "."))
with open(filePath + "/utils/relationStaticResult.txt", "r", encoding='utf8') as fr:
    for line in fr:
        relationNameCount = line.split(",")
        relationName = relationNameCount[0][2:-1]
        relationCount = relationNameCount[1][1:-2]
        relationCountDict[relationName] = int(relationCount)
    # print(relationCountDict)


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
    # print(len(relationDict))

    return relationDict


def entity(request):
    ctx = {}
    # 根据传入的实体名称搜索出关系
    if (request.GET):
        entity = request.GET['user_text']
        if entity is None:
            return render(request, 'entity.html', {'ctx': ctx})
        # 连接数据库
        db = neo_con
        if (entity.isdigit()):
            entityRelation = db.getEntityRelationbyEntity(entity)
            print(entityRelation)
            print("开始炸弹修")
            # print(entityRelation)
        else:
            entityRelation = db.getEntityRelationbyEntityText(entity)
        # print(json.dumps(entityRelation, ensure_ascii=False))
        # for i in entityRelation:
        #     print(list(i['rel'].types())[0])
        if len(entityRelation) == 0:
            # 若数据库中无法找到该实体，则返回数据库中无该实体
            ctx = {'title': '<h1>数据库中暂未添加该实体</h1>'}
            return render(request, 'entity.html', {'ctx': json.dumps(ctx, ensure_ascii=False)})
        else:
            # 返回查询结果
            # 将查询结果按照"关系出现次数"的统计结果进行排序
            entityRelation = sortDict(entityRelation)
            print("在这里")
            print(entityRelation)
            kk = json.dumps(entityRelation, ensure_ascii=False)
            # json.dumps() 是把python对象转换成json对象的一个过程，生成的是字符串。
            # print("dump后")
            # [{"rel": {}, "entity2": {"name": "Messaging System"}, "relationCount": 0}, {"rel": {}, "entity2":
            # json.loads()函数是将json格式数据转换为字典
            tt = json.loads(kk)
            # [{'rel': {}, 'entity2': {'name': 'Messaging System'}, 'relationCount': 0}, {'rel': {}, 'entity2'
            # 加入关系
            for i in range(len(entityRelation)):
                # print(tt[i]["rel"])
                tt[i]["rel"]["type"] = list(entityRelation[i]['rel'].types())[0]
                # print(tt[i]["rel"])
            # tt [{'rel': {'type': 'Component'}, 'entity2': {'name': 'Messaging System'}, 'relationCount': 0}, {'rel': {'type': 'Milestone'}, 'entity2':
            print(tt)
            print("=====================")
            print(json.dumps(tt, ensure_ascii=False))
            return render(request, 'entity.html', {'entityRelation': json.dumps(tt, ensure_ascii=False)})

    return render(request, "entity.html", {'ctx': ctx})


def search_relation(request):
    ctx = {}
    if (request.GET):
        db = neo_con
        entity1 = request.GET['entity1_text']
        relation = request.GET['relation_name_text']
        entity2 = request.GET['entity2_text']
        relation = relation.lower()
        searchResult = {}
        # 若只输入entity1,则输出与entity1有直接关系的实体和关系
        if (len(entity1) != 0 and len(relation) == 0 and len(entity2) == 0):
            searchResult = db.findRelationByEntity(entity1)
            searchResult = sortDict(searchResult)
            kk = json.dumps(searchResult, ensure_ascii=False)
            tt = json.loads(kk)
            # print("11111111111111111")
            for i in range(len(searchResult)):
                # print(tt[i]["rel"])
                tt[i]["rel"]["type"] = list(searchResult[i]['rel'].types())[0]
            #     print("111111111111111111")
            #     print(tt[i]["rel"])
            # print(json.dumps(tt, ensure_ascii=False))
            if (len(searchResult) > 0):
                return render(request, 'relation.html', {'searchResult': json.dumps(tt, ensure_ascii=False)})

        # 若只输入entity2则,则输出与entity2有直接关系的实体和关系
        if (len(entity2) != 0 and len(relation) == 0 and len(entity1) == 0):
            searchResult = db.findRelationByEntity2(entity2)
            searchResult = sortDict(searchResult)
            kk = json.dumps(searchResult, ensure_ascii=False)
            tt = json.loads(kk)
            # print("11111111111111111")
            for i in range(len(searchResult)):
                # print(tt[i]["rel"])
                tt[i]["rel"]["type"] = list(searchResult[i]['rel'].types())[0]
            if (len(searchResult) > 0):
                return render(request, 'relation.html', {'searchResult': json.dumps(tt, ensure_ascii=False)})
        # 若输入entity1和relation，则输出与entity1具有relation关系的其他实体
        if (len(entity1) != 0 and len(relation) != 0 and len(entity2) == 0):
            searchResult = db.findOtherEntities(entity1, relation)
            searchResult = sortDict(searchResult)
            print("开始啦")
            print(searchResult)
            if (len(searchResult) > 0):
                return render(request, 'relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        # 若输入entity2和relation，则输出与entity2具有relation关系的其他实体
        if (len(entity2) != 0 and len(relation) != 0 and len(entity1) == 0):
            searchResult = db.findOtherEntities2(entity2, relation)
            searchResult = sortDict(searchResult)
            if (len(searchResult) > 0):
                return render(request, 'relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        # 若输入entity1和entity2,则输出entity1和entity2之间的最短路径
        if (len(entity1) != 0 and len(relation) == 0 and len(entity2) != 0):
            searchResult = db.findRelationByEntities(entity1, entity2)
            if (len(searchResult) > 0):
                # print(searchResult)
                searchResult = sortDict(searchResult)
                return render(request, 'relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        # 若输入entity1,entity2和relation,则输出entity1、entity2是否具有相应的关系
        if (len(entity1) != 0 and len(entity2) != 0 and len(relation) != 0):
            searchResult = db.findEntityRelation(entity1, relation, entity2)
            if (len(searchResult) > 0):
                return render(request, 'relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        # 全为空
        if (len(entity1) != 0 and len(relation) != 0 and len(entity2) != 0):
            pass
        ctx = {'title': '<h1>暂未找到相应的匹配</h1>'}
        return render(request, 'relation.html', {'ctx': ctx})

    return render(request, 'relation.html', {'ctx': ctx})
