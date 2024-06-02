from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze.html', views.analyze, name='analyze'),
    path('download_report/', views.download_report, name='download_report'), 
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('procedure.html', views.procedure, name='procedure'),
]
