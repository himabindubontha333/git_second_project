from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def app1_first(request):
    return HttpResponse('This is the app1_first view function')
def app1_second(request):
    return HttpResponse('This is the app1_second view function')

def app2_first(request):
    return HttpResponse('This is the app2_first view function')
def app2_second(request):
    return HttpResponse('This is the app2_second view function')




