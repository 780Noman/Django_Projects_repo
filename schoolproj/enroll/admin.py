from django.contrib import admin
from enroll.models import Student
# Register your models here.
"""her table ke liye separate sy register kerna lazmi ha"""
#register  Model by Decorator 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname','stuemail','stupass','comment')
# admin.site.register(Student, StudentAdmin) #alter method for registering