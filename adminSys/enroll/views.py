from django.shortcuts import render,HttpResponseRedirect
from .forms import  SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
#when you want to create form with old password then used PasswordchangeFor
#when you want to create form without old password then used SetPasswordForm
#UserChangeForm it will show complete profile form
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.models import User,Group
'''
from django.views.decorators.cache import cache_page
@cache_page(30)
def home(request):
#now setting.py write code
    return render(request,'enroll/course.html')
'''

# Create your views here.
#signUp function based view
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully!!')
            user=fm.save()
            group= Group.objects.get(name='Editor')
            user.groups.add(group)
        else:
            messages.error(request,'Invalid Credentials!!')
    else:
        fm = SignUpForm()
    return render(request,'enroll/signup.html',{'form': fm})

#login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None and user.is_active:
                    login(request, user)
                    messages.success(request, 'Login Successfully!!')
                    # return HttpResponseRedirect('/profile/')
                    return HttpResponseRedirect('/dashboard/')
                else:
                    messages.error(request, 'Invalid username or password!!')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/dashboard/')
        # return HttpResponseRedirect('/profile/')

#profile
# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login/')
# def user_profile(request):
#     return render(request, 'enroll/profile.html', context={'name': request.user})
def user_profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST,instance=request.user)
                users = User.objects.all() 
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users = None
                
            if fm.is_valid():
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all() 
                
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', context={'name': request.user.username,'form':fm , 'users':users})
    else:
        messages.error(request, 'You need to log in to view this page.')
        return HttpResponseRedirect('/login/')



#logout
def user_logout(request):
    logout(request)  # Logs out the user
    messages.success(request, 'Logged out successfully.')
    return HttpResponseRedirect('/login/')

#change password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)  
        return render(request,'enroll/changepass.html',context={'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
def user_detail(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, 'enroll/userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")
'''Dashboard function'''    
def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'enroll/dashboard.html',context={'name':request.user.username})
    else:
        # messages.error(request, 'You need to log in to view this page.')
        return HttpResponseRedirect('/login/')
 
'''Cookies functions'''
def setcookie(request):
    respone = render(request,'enroll/setcookie.html')
    respone.set_signed_cookie('name','nomi',salt='nm')
    # respone.set_cookie('name','noman') #(key,value,max_age=100) pass kis jati ha  
    # respone.set_cookie('name','noman',expires=datetime.utcnow()+timedelta(days=2))  
    return respone

def getcookie(request):
    # nm = request.COOKIES['name'] #using key to get cookie data
    # nm=request.COOKIES.get('name')
    # nm=request.COOKIES.get('name','Guest')
    nm=request.get_signed_cookie('name',salt='nm',default='Guest')
    return render(request,'enroll/getcookie.html',context={'name':nm})

def delcookie(request):
    response = render(request,'enroll/delcookie.html')
    response.delete_cookie('name')
    return response
"""All code related to session framework"""
def setsession(request):
    request.session['name']='Noman'
    request.session['lname']='Amjad'
    return render(request,'enroll/setsession.html')
def getsession(request):
    # name=request.session['name']
    name=request.session.get('name',default="Guest")
    keys=request.session.keys()
    items=request.session.items()
    age=request.session.setdefault('age','21')
    return render(request,'enroll/getsession.html',{'name':name,'keys':keys,'items':items,'age':age})

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render(request,'enroll/delsession.html')