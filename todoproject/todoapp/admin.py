from django.contrib import admin
from todoapp.models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display=['title','description','status','date_time','created','updated']

admin.site.register(Todo,TodoAdmin)
