from py2neo import Graph, Node, Relationship, cypher, Path
import neo4j

from utils.read_csv_test import qidong


# 操作neo4j的类
class Neo4j:
    graph = None

    def __init__(self):
        print("create neo4j class ...")
        #qidong()

    # 初始化neo4j,建立连接
    def connectDB(self):
        self.graph = Graph("http://118.195.147.91:7474", username="neo4j", password="123456789")

    # 根据结点的title属性title返回结点
    def matchItembyname(self, value):
        sql = "MATCH (n:Bud_Id { name: '" + str(value) + "' }) return n;"
        answer = self.graph.run(sql).data()
        print(answer)
        return answer

    # [{'rel': Type(Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #                    Status='VERIFIED', Type='defect', name='108746'), Node('Type', name='defect')),
    #   'entity2': Node('Type', name='defect')}, {'rel': Severity(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Severity', name='critical')),
    #                                             'entity2': Node('Severity', name='critical')}, {'rel': Describe(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Describe', name='crash')), 'entity2': Node(
    #     'Describe', name='crash')}, {'rel': Describe(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Describe', name='open')),
    #                                  'entity2': Node('Describe', name='open')}, {'rel': Describe(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Describe', name='immediate')),
    #                                                                              'entity2': Node('Describe',
    #                                                                                              name='immediate')}, {
    #      'rel': Describe(
    #          Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #               Status='VERIFIED', Type='defect', name='108746'), Node('Describe', name='list properties')),
    #      'entity2': Node('Describe', name='list properties')}, {'rel': Describe(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Describe', name='select')),
    #                                                             'entity2': Node('Describe', name='select')}, {
    #      'rel': Describe(
    #          Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #               Status='VERIFIED', Type='defect', name='108746'), Node('Describe', name='cursor')),
    #      'entity2': Node('Describe', name='cursor')}, {'rel': Describe(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Describe', name='right click')),
    #                                                    'entity2': Node('Describe', name='right click')}, {
    #      'rel': Describe(
    #          Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #               Status='VERIFIED', Type='defect', name='108746'), Node('Describe', name='browser')),
    #      'entity2': Node('Describe', name='browser')}, {'rel': Describe(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Describe', name='edit page')),
    #                                                     'entity2': Node('Describe', name='edit page')}, {'rel': Status(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Status', name='VERIFIED')), 'entity2': Node(
    #     'Status', name='VERIFIED')}, {'rel': Priority(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Priority', name='Not set')),
    #                                   'entity2': Node('Priority', name='Not set')}, {'rel': Product(
    #     Node('BUG_ID', Component='Composer', Priority='Not set', Product='SeaMOnkey', Serverity='critical',
    #          Status='VERIFIED', Type='defect', name='108746'), Node('Product', name='defect')),
    #                                                                                  'entity2': Node('Product',
    #                                                                                                  name='defect')}]
    # # 根据title值返回互动百科item
    # def matchHudongItembyTitle(self, value):
    #     sql = "MATCH (n:HudongItem { title: '" + str(value) + "' }) return n;"
    #     try:
    #         answer = self.graph.run(sql).data()
    #     except:
    #         print(sql)
    #     return answer

    # 根据entity的名称返回关系（正向）
    def getEntityRelationbyEntity(self, value):
        answer = self.graph.run("MATCH (entity1) - [rel] -> (entity2)  WHERE entity1.name = \"" + str(
            value) + "\" RETURN rel,entity2 Limit 50").data()
        return answer

    # 根据entity的名称返回关系（反向）
    def getEntityRelationbyEntityText(self, value):
        answer = self.graph.run("MATCH (entity1) <- [rel] - (entity2)  WHERE entity1.name = \"" + str(
            value) + "\" RETURN rel,entity2 Limit 50").data()
        return answer

    # 查找entity1及其对应的关系（与getEntityRelationbyEntity的差别就是返回值不一样）
    def findRelationByEntity(self, entity1):
        answer = self.graph.run("MATCH (n1 {name:\"" + str(entity1) + "\"})- [rel] -> (n2) RETURN n1,rel,n2 Limit 50").data()
        # print(answer)
        # if(answer is None):
        # 	answer = self.graph.run("MATCH (n1:NewNode {title:\""+entity1+"\"})- [rel] -> (n2) RETURN n1,rel,n2" ).data()
        return answer

    # 查找entity2及其对应的关系
    def findRelationByEntity2(self, entity1):
        answer = self.graph.run(
            "MATCH (n1)- [rel] -> (n2 {name:\"" + str(entity1) + "\"}) RETURN n1,rel,n2 Limit 15").data()
        print(answer)

        # if(answer is None):
        # 	answer = self.graph.run("MATCH (n1)- [rel] -> (n2:NewNode {title:\""+entity1+"\"}) RETURN n1,rel,n2" ).data()
        return answer

    # 根据entity1和关系查找entity2
    def findOtherEntities(self, entity, relation):
        answer = self.graph.run("MATCH (n1 {name:\"" + str(entity) + "\"})- [rel {name:\"" + str(
            relation) + "\"}] -> (n2) RETURN n1,rel,n2").data()
        print(answer)
        # if(answer is None):
        #	answer = self.graph.run("MATCH (n1:NewNode {title:\"" + entity + "\"})- [rel:RELATION {type:\""+relation+"\"}] -> (n2) RETURN n1,rel,n2" ).data()

        return answer

    # 根据entity2和关系查找enitty1
    def findOtherEntities2(self, entity, relation):
        answer = self.graph.run("MATCH (n1)- [rel {name:\"" + str(relation) + "\"}] -> (n2 {name:\"" + str(
            entity) + "\"}) RETURN n1,rel,n2").data()
        # if(answer is None):
        #	answer = self.graph.run("MATCH (n1)- [rel:RELATION {type:\""+relation+"\"}] -> (n2:NewNode {title:\"" + entity + "\"}) RETURN n1,rel,n2" ).data()

        return answer

    # 根据两个实体查询它们之间的最短路径
    def findRelationByEntities(self, entity1, entity2):
        answer = self.graph.run("MATCH (p1:HudongItem {title:\"" + str(entity1) + "\"}),(p2:HudongItem{title:\"" + str(
            entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN rel").evaluate()
        # answer = self.graph.run("MATCH (p1:HudongItem {title:\"" + entity1 + "\"})-[rel:RELATION]-(p2:HudongItem{title:\""+entity2+"\"}) RETURN p1,p2").data()

        if (answer is None):
            answer = self.graph.run(
                "MATCH (p1:HudongItem {title:\"" + str(entity1) + "\"}),(p2:NewNode {title:\"" + str(
                    entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN p").evaluate()
        if (answer is None):
            answer = self.graph.run("MATCH (p1:NewNode {title:\"" + str(entity1) + "\"}),(p2:HudongItem{title:\"" + str(
                entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN p").evaluate()
        if (answer is None):
            answer = self.graph.run("MATCH (p1:NewNode {title:\"" + str(entity1) + "\"}),(p2:NewNode {title:\"" + str(
                entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN p").evaluate()
        # answer = self.graph.data("MATCH (n1:HudongItem {title:\"" + entity1 + "\"})- [rel] -> (n2:HudongItem{title:\""+entity2+"\"}) RETURN n1,rel,n2" )
        # if(answer is None):
        #	answer = self.graph.data("MATCH (n1:HudongItem {title:\"" + entity1 + "\"})- [rel] -> (n2:NewNode{title:\""+entity2+"\"}) RETURN n1,rel,n2" )
        # if(answer is None):
        #	answer = self.graph.data("MATCH (n1:NewNode {title:\"" + entity1 + "\"})- [rel] -> (n2:HudongItem{title:\""+entity2+"\"}) RETURN n1,rel,n2" )
        # if(answer is None):
        #	answer = self.graph.data("MATCH (n1:NewNode {title:\"" + entity1 + "\"})- [rel] -> (n2:NewNode{title:\""+entity2+"\"}) RETURN n1,rel,n2" )
        relationDict = []
        if (answer is not None):
            for x in answer:
                tmp = {}
                start_node = x.start_node
                end_node = x.end_node
                tmp['n1'] = start_node
                tmp['n2'] = end_node
                tmp['rel'] = x
                relationDict.append(tmp)
        return relationDict

    # 查询数据库中是否有对应的实体-关系匹配
    def findEntityRelation(self, entity1, relation, entity2):
        answer = self.graph.run("MATCH (n1:HudongItem {title:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
            relation) + "\"}] -> (n2:HudongItem{title:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()
        if (answer is None):
            answer = self.graph.run(
                "MATCH (n1:HudongItem {title:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
                    relation) + "\"}] -> (n2:NewNode{title:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()
        if (answer is None):
            answer = self.graph.run("MATCH (n1:NewNode {title:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
                relation) + "\"}] -> (n2:HudongItem{title:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()
        if (answer is None):
            answer = self.graph.run("MATCH (n1:NewNode {title:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
                relation) + "\"}] -> (n2:NewNode{title:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()

        return answer
