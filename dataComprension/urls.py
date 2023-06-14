
from django.urls import path
from . import views


urlpatterns = [
    path('resume-statistic', views.resumeState, name='index'),
    path('mising-data', views.misingDt, name='index'),
    path('data-zeros', views.dataZero, name='index'),
    path('data-outliders', views.dataOut, name='index'),
    path('all-data-zeros', views.allDataZero, name='index')
]