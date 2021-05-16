import json
import pickle
import zipfile

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import uuid
import os

from utils.auto_create import kankan


def to_fileupload(request):
    return render(request, 'annotate.html')

def kankan():
    path = os.getcwd() + '\\demo\\utils\dealed_words'
    with open('dealed_words', 'rb') as filehandle:
        load_list = pickle.load(filehandle)
    return load_list

def local(request):
    file = request.FILES.get('file')
    # print("我来了")
    # print(file)
    # print(request.FILES.get('file[]'))
    # print(request)
    if not file:
        return HttpResponse('请选择要导入的文件！<a href="/annotating/">返回</a> ')

    # file_name = os.getcwd()+'\\demo\\temp\\{}_{}_{}'.format(uuid.uuid4(), datetime.now().strftime('%Y-%m-%d-%H-%M-%S'), file.name)
    path = os.getcwd() + '\\demo\\temp\\{}_{}_{}'.format(uuid.uuid4(), datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
                                                         file.name)
    with open(path, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    zfile = zipfile.ZipFile(path, "r")
    kk = ""
    star = ""
    for item in zfile.namelist():
        if item.endswith(".txt"):
            zfile.extract(item, os.getcwd() + '\\demo\\temp\\txt')
    zfile.close()
    for item in zfile.namelist():
        if item.endswith(".txt"):
            txt_path = os.getcwd() + '\\demo\\temp\\txt\\' + item
            f = open(txt_path, "r", encoding='utf-8')
            star = star + " " + f.read()
    f.close()
    # print(star)
    ctx = {}
    ctx["rlt"] = star
    load_list = kankan()
    print(load_list)
    return render(request, "annotate.html", ctx)


def local_a(request):
    print(request.is_ajax())
    file = request.FILES.get('file[]')
    # if not file:
    #     return HttpResponse('请选择要导入的文件！<a href="/annotating/">返回</a> ')

    # file_name = os.getcwd()+'\\demo\\temp\\{}_{}_{}'.format(uuid.uuid4(), datetime.now().strftime('%Y-%m-%d-%H-%M-%S'), file.name)
    path = os.getcwd() + '\\demo\\temp\\{}_{}_{}'.format(uuid.uuid4(), datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
                                                         file.name)
    with open(path, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    zfile = zipfile.ZipFile(path, "r")
    kk = ""
    star = ""
    for item in zfile.namelist():
        if item.endswith(".txt"):
            zfile.extract(item, os.getcwd() + '\\demo\\temp\\txt')
    zfile.close()
    for item in zfile.namelist():
        if item.endswith(".txt"):
            txt_path = os.getcwd() + '\\demo\\temp\\txt\\' + item
            f = open(txt_path, "r", encoding='utf-8')
            star = star + f.read()
    star = star + "***************"
    f.close()
    ctx = {}
    ctx['rlt'] = star
    print(ctx)
    return HttpResponse(json.dumps(ctx, ensure_ascii=False))
    # return HttpResponse(star)
    # return redirect("/login")
