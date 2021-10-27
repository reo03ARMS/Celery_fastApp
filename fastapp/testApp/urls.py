from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('celery_test/', views.celery_test, name='celery_test'),
    path('ai_bot/',views.AI_chatBot,name="ai_bot")
]