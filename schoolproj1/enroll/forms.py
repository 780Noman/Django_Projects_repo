from django import forms
#for built-in validation using 
from django.core import validators

class StudentReg(forms.Form):  
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)]) #custom validation bi kr sakty phir func ka name pass ker do list ma
    
    
    # agree = forms.BooleanField( label_suffix='',label='I agree')
    # name= forms.CharField(min_length=5, max_length=10,strip=False,
    #                                         empty_value='Nomi',error_messages={'required':'Enter your Name'})
    # roll=forms.IntegerField(min_value=5,max_value=40)
    # price=forms.DecimalField(min_value=5,max_value=50,max_digits=4, decimal_places=1)
    # rate= forms.FloatField(min_value=4,max_value=40)
    name= forms.CharField()
    email= forms.EmailField(required=False)
    password= forms.CharField(widget=forms.PasswordInput)
    repassword= forms.CharField(label='password Re-enter',widget=forms.PasswordInput)
    
    
    #jabh single field pr validation use kerni ho
    def clean_name(self):
        valname = self.cleaned_data['name']
        if  len(valname)<5:
            raise forms.ValidationError("Enter more than 5  character")
        else:
            return valname
        
        
    #jabh full form pr validation use kerni ho 
    def clean(self):
        cleaned_data = super().clean()
        valname= self.changed_data['name']
        valemail= self.cleaned_data['email']
        if len(valname)<5:
            raise forms.ValidationError('name should be more than 5 character')
        if len(valemail)<5:
            raise forms.ValidationError('Email should be more than 5 character')
    
    """Password Matching and reenter password"""
    def clean(self):
        cleaned_data = super().clean()
        valpassword = self.cleaned_data['password']
        valrepassword = self.cleaned_data['repassword']
        if valpassword != valrepassword:
            raise forms.ValidationError('Password and Re-enter password should be same')
            
        
