from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('doc', views.doc, name='page3'),
    path('adr', views.adr, name='page4')
    ]
