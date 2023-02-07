from django.contrib import admin
from Teachers.models import *
# Register your models here.
# admin.site.register(TeachersData)

class TeachersDataAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "profile_picture", "email_address", "phone_number", "room_number", "subjects_taught")
    search_fields = ['first_name','last_name', 'subjects_taught']

admin.site.register(TeachersData, TeachersDataAdmin)