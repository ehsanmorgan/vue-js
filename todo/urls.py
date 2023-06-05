from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import todolist
from .api import TodolistApi







router = DefaultRouter()
router.register('',TodolistApi)


urlpatterns = [
    path('todolist',todolist),
    path('api/', include(router.urls)),
    
]

