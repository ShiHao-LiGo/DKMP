import requests
import json

data = {
 "t": "Steps to reproduce: 1. Open browser 2. Visit http://www.mozilla.org/mailnews/specs/folder/ 3. Right-click, select Edit Page in Composer 3. Place cursor in the text of the list of bugs 4. Right-click in the text, select \"List Properties\" Expected Results: Open a dialog to edit the list properties Actual Results: Immediate crash. Reproducable: 100%. Using trunk build pulled a few hours ago (post darin backout), glibc2.2, gcc-3.0.2 K6-2 300 on Debian sid."
}
headers = {'Content-Type': 'application/json'} ## headers中添加上content-type这个参数，指定为json格式
an = []
response = requests.post(url='http://localhost:5006/person/extract', headers=headers, data=json.dumps(data)) ## post的时候，将data字典形式的参数用json包转换成json格式。
datas = json.loads(response.text)
for key in datas:
    if datas[key] !=[]:
        an = an + datas[key]

print(list(set(an)))