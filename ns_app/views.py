from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # print(request.META['sasas'])
    html = """
    <div style='width=100%;height:50px;background-color:#555'>
    <a href='http://127.0.0.1:8000/about'>kirish</a>
    </div>
    """
    return HttpResponse(html)


def about(request, num1, num2):
    # print(request.META['sasas'])
    # html = """
    # <div style='width=100%;height:50px;background-color:red'>
    #
    # </div>
    # """
    html = f"<h1>Your number:{num1 + num2}</h1>"

    return HttpResponse(html)
