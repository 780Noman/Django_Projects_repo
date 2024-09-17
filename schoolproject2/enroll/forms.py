from django import forms
#for built-in validation using 
# from django.core import validators

class StudentReg(forms.Form):  
    # error_css_class='error'
    # required_css_class='required'
    name= forms.CharField(error_messages={'required':'Enter your name'})
    email= forms.EmailField(error_messages={'required': 'Enter your email'})
    password= forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter your password'})
  
            
        
