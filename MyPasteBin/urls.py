from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-text', views.add, name='add'),
    path('history', views.history, name='history'),
]