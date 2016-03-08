from django.contrib import admin

from .models import *


#admin.site.register(Snake)
class SnakeAdmin(admin.ModelAdmin):
    list_display = ('name_separated','snake_thumbnail', 'location',)
    search_fields = ['name_separated','location']

class KindAdmin(admin.ModelAdmin):
    list_display = ('name_separated','kind_thumbnail',)
    search_fields = ['name_separated',]
admin.site.register(Kind,KindAdmin)
admin.site.register(Snake, SnakeAdmin)