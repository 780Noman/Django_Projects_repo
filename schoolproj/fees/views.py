from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fees_dj(request):
    return render(request,'fees/fees1.html')

def fees_py(request):
    return render(request, 'fees/fees2.html')
# Create your views here.
