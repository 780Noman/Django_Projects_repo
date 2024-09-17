from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentReg

def thankyou(request):
    return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)       
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            repassword = fm.cleaned_data['repassword']
            # rate= fm.cleaned_data['rate']
            print('Name:', name)
            print('Email:', email)
            print('Password:', password)
            print('Password ReEnter:', repassword)
            # print('Rate:', rate)
            return HttpResponseRedirect('/regi/success')
        else:
            # If the form is invalid, re-render the form with errors
            return render(request, 'enroll/userReg.html', context={'form': fm})
    else:
        fm = StudentReg()
        return render(request, 'enroll/userReg.html', context={'form': fm})

    # The view will always return an HttpResponse, so no additional else block is necessary
