import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# data = "What's the type of bug-108746？"
# stopWords = set(stopwords.words('english'))
# words = word_tokenize(data)
# wordsFiltered=[]
# for w in words:
#     if w not in stopWords:
#         wordsFiltered.append(w)
# print(wordsFiltered)
import re
#正则提取Bugid
# BugID = re.findall(r'\d+',"Bug-108746's description？")
# str = "Bug-108746's description？"
# print(BugID[0])
# Bug_ID = models.CharField(max_length=30)
# title = models.TextField(null=True)
# product = models.TextField(null=True)
# component = models.TextField(null=True)
# Type = models.TextField(null=True)
# Priority = models.TextField(null=True)
# Severity = models.TextField(null=True)
# Status = models.TextField(null=True)
# Milestone = models.TextField(null=True)
# comment = models.TextField(null=True)
# models.DATAs.objects.create(BugID="108746",title ="Crash opening List Properies dialog",product="SeaMonkey",Type="defect",Priority="Not set",Severity="critical",Status="VERIFIED",Milestone="",comment="Steps to reproduce:1. Open browser 2. Visit http://www.mozilla.org/mailnews/specs/folder/ 3. Right-click, select Edit Page in Composer 4. Place cursor in the text of the list of bugs 5. Right-click in the text, select "List Properties" Expected Results: Open a dialog to edit the list properties Actual Results: Immediate crash. Reproducable: 100%. Using trunk build pulled a few hours ago (post darin backout), glibc2.2, gcc-3.0.2 K6-2 300 on Debian sid.")
#对How,what+describe,symptom,symptons,症状,原因,怎么，如何
#返回Bug描述和图谱