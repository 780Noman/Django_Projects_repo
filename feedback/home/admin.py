from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(CustomerFeedback)
admin.site.register(CustomerResponse)