import pandas as pd  # 导入pandas包

# -*-encoding:utf-8-*-
import csv

# 读取csv文件
from rabc.models import DATAs
def qidong():
    with open("G:/pythonlearn/mykg/utils/text.csv", "r",encoding='utf-8') as f:
        reader = csv.reader(f)
        i=1
        for row in reader:
            print(i)
            i=i+1
            DATAs.objects.create(Bug_ID=row[0],title=row[1],product=row[2],component=row[3],Type=row[4],Priority=row[5],Severity=row[6],Status=row[7],Milestone=row[8],comment=row[9])

