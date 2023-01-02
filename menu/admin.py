from django.contrib import admin

# Register your models here.
from .models import MenuTree


class MenuTreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'menuName', 'parent')
    list_filter = ('menuName',)


admin.site.register(MenuTree, MenuTreeAdmin)
