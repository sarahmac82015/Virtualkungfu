from django.contrib import admin
from .models import TestedForm, FormL
from home.models import User

# Register your models here.
class TestedFormAdmin(admin.ModelAdmin):
    pass

admin.site.register(TestedForm, TestedFormAdmin)

#class FormL(admin.ModelAdmin):
#    pass

#admin.site.register(FormL, FormLAdmin)

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)

