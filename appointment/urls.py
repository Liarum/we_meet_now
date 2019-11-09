from django.urls import path
from  . import views

urlpatterns = [
    path('home/', views.index, name="homepage"),
    path('meeting/', views.meeting, name="meeting"),
    path('schedule/<int:id>/', views.schedule, name="schedule"),
]