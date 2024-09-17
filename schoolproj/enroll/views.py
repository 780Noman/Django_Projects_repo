from django.shortcuts import render
from enroll.models import Student
from .forms import StudentReg
# Create your views here.

def showformdata(request):
    if  request.method == 'POST':
        fm = StudentReg(request.POST)
        
        if fm.is_valid():
            # name=request.POST['name']
            # print(name )
            # print(fm)
            name = fm.cleaned_data['name']
            email= fm.cleaned_data['email']
            print('Name :',name)
            print('Email :',email)
            print('Ye POST request se aya hai')
            
    else:
        fm = StudentReg()
        print('ya get request sy aya ha ')
    # fm = StudentReg(auto_id=True, label_suffix=' ',initial={'name':'Noman'}) # auto_id=False , 'zyx'
    # fm.order_fields(field_order=['email','name'])
    return render(request,'enroll/userReg.html',context={'form': fm }) 
def studentinfo(request):
    stud = Student.objects.all()
    # stud = Student.objects.get(pk=2) # jabh koi specific object chaye ho to 
    
    print("Output : ",stud)
    return render(request,'enroll/studetails.html',context={'stu' : stud})