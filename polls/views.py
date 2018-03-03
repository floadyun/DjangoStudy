from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return HttpResponse("Hello Wrord!")

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = 'You are looking at the results of question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)

def error(request):
    raise Http404('页面错误')
