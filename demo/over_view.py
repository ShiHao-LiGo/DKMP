import json

from django.shortcuts import render

from demo.entity_view import sortDict
from utils.pre_load import neo_con

ctx = {}
# 根据传入的实体名称搜索出关系
# def over_view(request):
#     if (request.GET):
#         entity = "108746"
#         # 连接数据库
#
#         db = neo_con
#         if (entity.isdigit()):
#             entityRelation = db.getEntityRelationbyEntity(entity)
#         else:
#             entityRelation = db.getEntityRelationbyEntityText(entity)
#         # print(json.dumps(entityRelation, ensure_ascii=False))
#         # for i in entityRelation:
#         #     print(list(i['rel'].types())[0])
#         if len(entityRelation) == 0:
#             # 若数据库中无法找到该实体，则返回数据库中无该实体
#             ctx = {'title': '<h1>数据库中暂未添加该实体</h1>'}
#             return render(request, 'entity.html', {'ctx': json.dumps(ctx, ensure_ascii=False)})
#         else:
#             # print("111111")
#             # 返回查询结果
#             # 将查询结果按照"关系出现次数"的统计结果进行排序
#             entityRelation = sortDict(entityRelation)
#             kk = json.dumps(entityRelation, ensure_ascii=False)
#             tt = json.loads(kk)
#             # print(tt)
#             for i in range(len(entityRelation)):
#                 print(tt[i]["rel"])
#                 tt[i]["rel"]["type"] = list(entityRelation[i]['rel'].types())[0]
#                 print(tt[i]["rel"])
#             # logging.debug(json.dumps(entityRelation, ensure_ascii=False))
#
#             return render(request, 'entity.html', {'entityRelation': json.dumps(tt, ensure_ascii=False)})
#
#     return render(request, "entity.html", {'ctx': ctx})

def over_view(request):
    ctx = {}
    entity = "108746"
    # 连接数据库

    db = neo_con
    entityRelation = db.getEntityRelationbyEntity(entity)
    # print(json.dumps(entityRelation, ensure_ascii=False))
    # for i in entityRelation:
    #     print(list(i['rel'].types())[0])
    if len(entityRelation) == 0:
        # 若数据库中无法找到该实体，则返回数据库中无该实体
        ctx = {'title': '<h1>数据库中暂未添加该实体</h1>'}
        return render(request, 'entity.html', {'ctx': json.dumps(ctx, ensure_ascii=False)})
    else:
        # print("111111")
        # 返回查询结果
        # 将查询结果按照"关系出现次数"的统计结果进行排序
        entityRelation = sortDict(entityRelation)
        kk = json.dumps(entityRelation, ensure_ascii=False)
        tt = json.loads(kk)
        # print(tt)
        for i in range(len(entityRelation)):
            # print(tt[i]["rel"])
            tt[i]["rel"]["type"] = list(entityRelation[i]['rel'].types())[0]
            # print(tt[i]["rel"])
        # logging.debug(json.dumps(entityRelation, ensure_ascii=False))

        return render(request, 'over_view.html', {'entityRelation': json.dumps(tt, ensure_ascii=False)})