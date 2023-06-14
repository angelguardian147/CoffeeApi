from django.shortcuts import render
from django.http import HttpResponse
from .analitycs.statistic import resumeStatistic, misingData, allDataInZero
from .analitycs.cleaning import dataInZero, dataOutliders

# Create your views here.

def resumeState(request):
    return HttpResponse(resumeStatistic())

def allDataZero(request):
    return HttpResponse(allDataInZero())

def dataZero(request):
    return HttpResponse(dataInZero())

def misingDt(request):
    return HttpResponse(misingData())

def dataOut(request):
    return HttpResponse(dataOutliders())