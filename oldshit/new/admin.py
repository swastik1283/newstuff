from django.contrib import admin
from new.models import Contact
# Register your models here.

class contact_admin(admin.ModelAdmin):
    list_display= ['name', 'email', 'phone', 'Query', 'date']
admin.site.register(Contact,contact_admin)