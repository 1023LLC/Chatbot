from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'blog\index.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)