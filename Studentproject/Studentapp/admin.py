from django.contrib import admin

from Studentapp.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','email','password','address','state','zip','mark']