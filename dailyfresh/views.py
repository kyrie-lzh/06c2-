from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    """
    首页
    :param request:
    :return:
    """
    return HttpResponse("欢迎来到首页")
