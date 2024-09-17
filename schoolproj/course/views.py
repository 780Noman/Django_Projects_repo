from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def learn_dj(request):
    return render(request,'course/courseinfo.html')

