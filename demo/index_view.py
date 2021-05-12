from django.shortcuts import render


def index(request):
    name = request.session.get('username')
    # print(name)
    if name :
        return render(request, "index.html", {'username':name})
    return render(request,"index.html",None)