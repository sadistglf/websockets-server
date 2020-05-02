from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/<str:roomId>/user/<str:username>/', views.postMessage, name='post-message')
]