from django.urls import path, include, re_path
from .views import *
from rest_framework import routers

urlpatterns = [
    path('women/', WomenListCreateApiView.as_view()),
    path('women/<int:pk>/', WomenRetrieveUpdateApiView.as_view()),
    path('womendelete/<int:pk>/', WomenRetrieveDelete.as_view()),
    path('women/drf-auth/', include('rest_framework.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path(r'^auth/', include('djoser.urls')),

]



