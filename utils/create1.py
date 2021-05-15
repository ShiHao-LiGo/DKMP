import ast
import json
import nltk
from py2neo import Graph, Node, Relationship
# import pandas as pd
import csv

# 读取数据
# -*-encoding:utf-8-*-
import csv


def str2list(str0):
    # 将字符串形式的列表转化为list
    str1 = str0.strip('[')
    str1 = str1.strip(']')
    str = str1.replace("'", "")
    str1 = str.split(',')
    return str1


def neo4j_build():
    # 连接neo4j数据库，输入地址、用户名、密码
    graph = Graph("http://localhost:7474", username="neo4j", password='123456789')
    # graph.delete_all()
    # 读取csv文件
    with open("bug_dealed_row.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        # for i in range(9):
        #     print(data[1][i])
        for i in range(5285,len(data)):
            print(i)
            # extra = {}
            # extra['name'] = data[i][0]
            # extra['product'] = data[i][1]
            # extra['component'] = data[i][2]
            # extra['Type'] = data[i][3]
            # extra['Priority'] = data[i][4]
            # extra['Severity'] = data[i][5]
            # extra['Status'] = data[i][6]
            # extra['Milestone'] = data[i][7]
            # extra['Describe'] = data[i][8]
            # print(extra)
            node_ID = Node('Bud_Id', name=data[i][0], product=data[i][1], component=data[i][2], Type=data[i][3],
                           Priority=data[i][4], Severity=data[i][5], Status=data[i][6], Milestone=data[i][7])
            node_product = Node('product', name=data[i][1])
            node_component = Node('component', name=data[i][2])
            node_Type = Node('Type', name=data[i][3])
            node_Priority = Node('Priority', name=data[i][4])
            node_Severity = Node('Severity', name=data[i][5])
            node_Status = Node('Status', name=data[i][6])
            node_Milestone = Node('Milestone', name=data[i][7])
            graph.create(node_ID)
            graph.create(node_product)
            graph.create(node_component)
            graph.create(node_Type)
            graph.create(node_Priority)
            graph.create(node_Severity)
            graph.create(node_Status)
            graph.create(node_Milestone)
            Rel1 = Relationship(node_ID, 'Product', node_product, name=data[i][1])
            Rel2 = Relationship(node_ID, 'Component', node_component, name=data[i][2])
            Rel3 = Relationship(node_ID, 'Type', node_Type, name=data[i][3])
            Rel4 = Relationship(node_ID, 'Priority', node_Priority, name=data[i][4])
            Rel5 = Relationship(node_ID, 'Severity', node_Severity, name=data[i][5])
            Rel6 = Relationship(node_ID, 'Status', node_Status, name=data[i][6])
            Rel7 = Relationship(node_ID, 'Milestone', node_Milestone, name=data[i][7])
            graph.create(Rel1)
            graph.create(Rel2)
            graph.create(Rel3)
            graph.create(Rel4)
            graph.create(Rel5)
            graph.create(Rel6)
            graph.create(Rel7)
            str1 = str2list(data[i][8])
            # print(str1[0])

            for k in range(len(str1)):
                t = Node('Describe', name=str1[k])
                graph.create(t)
                relation = Relationship(node_ID, 'Describe', t, name=str1[k])
                graph.create(relation)

            # describe_data = json.loads(data[i][8])
            # print(type(describe_data))

    # extra = {'name':'123','it':'小黄鸡oh给你','whta' :'大红'}
    # node = Node('huhu', **extra)
    # attr1 = Node('xixi', name="defect")
    #
    # Rel1 = Relationship(node, 'Product', attr1,name = "product")
    # graph.create(node)
    # graph.create(Rel1)
    #             Type=data[i][4], Priority=data[i][5], Serverity=data[i][6], Status=data[i][7], Milestone=data[i][8],
    #             Comment=data[i][9])
    # for row in reader:
    #     print(row)


# with open('bug_dealed_row.csv', 'r',newline='',encoding='utf-8') as f: reader = csv.reader(f) data = list(reader)
# print(data[2]) print(len(data)) print(data[1][0]) for i in range(1, len(data)): # node = Node('BUG_ID',
# name=data[i][0]) node = Node('BUG_ID', name=data[i][0], Title=data[i][1], Product=data[i][2],Component =data[i][3],
# Type= data[i][4],Priority =data[i][5],Serverity = data[i][6],Status=data[i][7],Milestone=data[i][8],Comment=data[
# i][9]) attr1 = Node('Product', name=data[i][2]) node = Node('BUG_ID',name = "108746",Product="SeaMOnkey",
# Component = "Composer",Type = "defect",Priority = "Not set",Serverity = "critical",Status="VERIFIED") attr2 = Node(
# 'Component', name=data[i][3]) attr3 = Node('Type', name=data[i][4]) attr4 = Node('Priority', name=data[i][5]) attr5
# = Node('Severity', name=data[i][6])

#     attr6 = Node('Status', name=data[i][7])
#     attr7 = Node('Milestone', name=data[i][8])
#     attr8 = Node('Title',name=data[i][1])
#     attr9 = Node('Comment',name = data[i][9])
# attr1 = Node('Product', name="defect")
# attr2 = Node('Composer', name="Not set")
# attr7 = Node('Severity', name="critical")
# attr3 = Node('Type', name="defect")
# attr4 = Node('Priority', name="Not set")
# attr5 = Node('Severity', name="critical")
# attr6 = Node('Status', name="VERIFIED")
# attr8 = Node('Describe', name="edit page")
# attr9 = Node('Describe', name="browser")
# attr10 = Node('Describe', name="right click")
# attr11 = Node('Describe', name="cursor")
# attr12 = Node('Describe', name="select")
# attr13 = Node('Describe', name="list properties")
# attr14 = Node('Describe', name="immediate")
# attr15 = Node('Describe', name="open")
# attr16 = Node('Describe', name="crash")
# graph.create(node)
# graph.create(attr1)
# graph.create(attr2)
# graph.create(attr3)
# graph.create(attr4)
# graph.create(attr5)
# graph.create(attr6)
# graph.create(attr7)
# graph.create(attr8)
# graph.create(attr9)
# graph.create(attr10)
# graph.create(attr11)
# graph.create(attr12)
# graph.create(attr13)
# graph.create(attr14)
# graph.create(attr15)
# graph.create(attr16)
# Rel1 = Relationship(node, 'Product', attr1)
# Rel2 = Relationship(node, 'Component', attr2)
# Rel3 = Relationship(node, 'Type', attr3)
# Rel4 = Relationship(node, 'Priority', attr4)
# Rel5 = Relationship(node, 'Severity', attr5)
# Rel6 = Relationship(node, 'Status', attr6)
# Rel7 = Relationship(node, 'Milestone', attr7)
# Rel8 = Relationship(node, 'Title', attr8)
# Rel9 = Relationship(node, 'Comment', attr9)
# Rel1 = Relationship(node, 'Product', attr1)
# Rel3 = Relationship(node, 'Type', attr3)
# Rel4 = Relationship(node, 'Priority', attr4)
# Rel5 = Relationship(node, 'Severity', attr5)
# Rel6 = Relationship(node, 'Status', attr6)
# Rel10 = Relationship(node, 'Describe', attr8)
# Rel11 = Relationship(node, 'Describe', attr9)
# Rel12 = Relationship(node, 'Describe', attr10)
# Rel13 = Relationship(node, 'Describe', attr11)
# Rel14 = Relationship(node, 'Describe', attr12)
# Rel15 = Relationship(node, 'Describe', attr13)
# Rel16 = Relationship(node, 'Describe', attr14)
# Rel17 = Relationship(node, 'Describe', attr15)
# Rel18 = Relationship(node, 'Describe', attr16)
# graph.create(Rel1)
# graph.create(Rel3)
# graph.create(Rel4)
# graph.create(Rel5)
# graph.create(Rel6)
# graph.create(Rel10)
# graph.create(Rel11)
# graph.create(Rel12)
# graph.create(Rel13)
# graph.create(Rel14)
# graph.create(Rel15)
# graph.create(Rel16)
# graph.create(Rel17)
# graph.create(Rel18)
# graph.run('MATCH (n:huhu) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
#           'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
def reduce():
    graph = Graph("http://localhost:7474", username="neo4j", password='123456789')
    graph.run('MATCH (n:Describe) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
              'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
    graph.run('MATCH (n:Priority) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
              'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
    graph.run('MATCH (n:Severity) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
              'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
    graph.run('MATCH (n:Status) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
              'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
    graph.run('MATCH (n:Type) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
              'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
    graph.run('MATCH (n:Product) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
              'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
    graph.run('MATCH (n:Product) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
              'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
    graph.run('MATCH (n:Milestone) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
              'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
    graph.run('MATCH (n:Component) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL '
              'apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')


# graph.run('MATCH (entity1:person) , (entity2:major{name:entity1.major}) CREATE (entity1)-[:研究]->(entity2)')
# graph.run('MATCH (entity1:person) , (entity2:univer{name:entity1.univer}) CREATE (entity1)-[:学校]->(entity2)')
# graph.run('MATCH (entity1:person) , (entity2:level{name:entity1.level}) CREATE (entity1)-[:学位]->(entity2)')
if __name__ == '__main__':
    neo4j_build()
    #reduce()
