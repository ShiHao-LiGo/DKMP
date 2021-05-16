from django.shortcuts import render


def relation(request):
    return render(request, "up_load.html", None)

def testtupu(request):
    return render(request,"tupuceshi.html",None)