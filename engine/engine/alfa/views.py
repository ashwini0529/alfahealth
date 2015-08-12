from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello. Index Configured for AlfaHealth")
# Create your views here.
def detail(request, user_id):
    return HttpResponse("You're looking at exercise %s." % user_id)

def results(request, user_id):
    response = "You're looking at the results of exercise %s."
    return HttpResponse(response % user_id)

def vote(request, user_id):
    return HttpResponse("You're voting on exercise %s." % user_id)
