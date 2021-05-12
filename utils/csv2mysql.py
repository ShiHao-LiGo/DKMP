# import pymysql
# import csv
# import codecs
#
#
# def get_conn():
#     conn = pymysql.connect(host='rm-uf6u5vvw69rjmftr23o.mysql.rds.aliyuncs.com', port=3306, user='test_01', passwd='Lsh123456789', db='kg_db', charset='utf8')
#     return conn
#
#
# def insert(cur, sql, args):
#     cur.execute(sql, args)
#
#
# def read_csv_to_mysql(filename):
#     with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         head = next(reader)
#         conn = get_conn()
#         cur = conn.cursor()
#         sql = 'insert into(Bug_ID,title,product,component,Type,Priority,Severity,Status,Milestone,comment) ' \
#               'demo_bug_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
#         for item in reader:
#             if item[1] is None or item[1] == '':  # item[1]作为唯一键，不能为null
#                 continue
#             args = tuple(item)
#             print(args)
#             insert(cur, sql=sql, args=args)
#
#         conn.commit()
#         cur.close()
#         conn.close()
#
#
# if __name__ == '__main__':
#     read_csv_to_mysql('G:/pythonlearn/mykg/utils/text.csv')

import pandas as pd
import pymysql
import csv
import codecs

def get_conn():
    db = pymysql.connect(host='rm-uf6u5vvw69rjmftr23o.mysql.rds.aliyuncs.com',
                         user='test_01',
                         password='Lsh123456789',
                         database='kg_db',
                         charset='utf8')
    return db
def insert(cur, sql, args):
    try:
        cur.execute(sql, args)
    except Exception as e:
        print(e)


def read_csv_to_mysql(filename):
    '''
    csv文件->数据库
    :param filename:
    :return:
    '''
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        # print(head)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into demo_bug_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for item in reader:
            # if item[1] is None or item[1] == '':  # item[1]作为唯一键，不能为null
            #     continue
            args = tuple(item)
            # print(args)
            insert(cur, sql=sql, args=args)

        conn.commit()
        cur.close()
        conn.close()

if __name__ == '__main__':
    read_csv_to_mysql('G:/pythonlearn/mykg/utils/text.csv')