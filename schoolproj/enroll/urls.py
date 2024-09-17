from django.urls import path
from . import views

urlpatterns = [
    path('stu/',views.studentinfo),
    path('reg/',views.showformdata),
]