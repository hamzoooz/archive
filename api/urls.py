from django.urls import path
from . import views 
urlpatterns = [
    path('', views.listbook, name='listbook' ),
    path('uplaod/', views.index, name='index' ),
]
