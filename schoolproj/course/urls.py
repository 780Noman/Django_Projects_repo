from django.urls import path
# from . import views  # it will call func using views.func
from .views import * # its will import everything
urlpatterns = [
    path('dj/',learn_dj,name='course'),
    # path('py/',learn_py),
]
