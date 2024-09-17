from django.urls import path
# from . import views  # it will call func using views.func
from .views import * # its will import everything
urlpatterns = [
    path('dj/',fees_dj),
    path('py/',fees_py),
]
