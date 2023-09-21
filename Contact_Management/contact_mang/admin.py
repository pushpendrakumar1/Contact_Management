from django.contrib import admin

from contact_mang.models import Contact

class con(admin.ModelAdmin):

    list_display = ('name','email','number')    
    

admin.site.register(Contact, con)
