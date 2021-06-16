import json

from django.http import HttpResponse
from django.shortcuts import render
import requests


def get_data(request):
    if request.method == 'POST':
        print('-----------')
        data = json.loads(request.body)
        if data == None or data == []:
            print('EMPTY')
        print(data)
    return HttpResponse("ok")
