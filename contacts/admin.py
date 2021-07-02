from django.contrib import admin
from . models import  contacts
# Register your models here.
class contact_admin(admin.ModelAdmin):
    list_display=('id','name','listing','email','contact_date')
    list_display_links=('id','name')
    search_fields=('name','email','listing')
    list_per_page=30


admin.site.register(contacts,contact_admin)