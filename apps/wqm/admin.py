from wqm.models import WqmAuthority,WqmArea
from django.contrib import admin
from hq.models import *
from resources.models import *
from django.contrib import admin



class WqmAuthorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified', 'created')
admin.site.register(WqmAuthority, WqmAuthorityAdmin)

class WqmAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'wqmauthority', 'modified', 'craeted')
admin.site.register(WqmArea, WqmAreaAdmin)

