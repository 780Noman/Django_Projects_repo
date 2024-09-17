from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentReg
from .models import User

def thankyou(request):
    return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)       
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            #taking same name of para  that  models class User have
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            # rate= fm.cleaned_data['rate']            
            # print('Rate:', rate)
            return HttpResponseRedirect('/regi/success')
        else:
            # If the form is invalid, re-render the form with errors
            return render(request, 'enroll/userReg.html', context={'form': fm})
    else:
        fm = StudentReg()
        return render(request, 'enroll/userReg.html', context={'form': fm})

    # The view will always return an HttpResponse, so no additional else block is necessary
