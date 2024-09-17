from django import forms

class StudentReg(forms.Form):
    name= forms.CharField(required=False)
    email= forms.EmailField(required=False)
    mobile=forms.IntegerField(required=False)
    key= forms.CharField(widget=forms.HiddenInput,required=False) #froms.textarea , forms.CheckboxInput, forms.FileInput
    # # key= forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1','id':'uniqueId'})) #froms.textarea , forms.CheckboxInput, forms.FileInput
    # f_name=forms.CharField(label='father Name',label_suffix="",
    #                        help_text='limit 50 char',disabled=True,required=False,initial='Muhammad')