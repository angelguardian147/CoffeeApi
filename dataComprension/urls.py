
from django.urls import path
from . import views


urlpatterns = [
    path('resume-statistic', views.resumeState, name='index'),
    path('mising-data', views.misingDt, name='index')
]