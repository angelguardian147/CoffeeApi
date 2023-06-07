from django.shortcuts import render
from django.http import HttpResponse
from .analitycs.statistic import resumeStatistic, misingData

# Create your views here.

def resumeState(request):
    return HttpResponse(resumeStatistic())


def misingDt(request):
    return HttpResponse(misingData())