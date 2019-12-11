from django.contrib import admin
from .models import Todo # add this
from .models import person

class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description', 'completed') # add this

class personAdmin(admin.ModelAdmin):  # add this
    list_display = ('first_name', 'last_name') # add this

# Register your models here.
admin.site.register(Todo, TodoAdmin) # add this
admin.site.register(person, personAdmin)
