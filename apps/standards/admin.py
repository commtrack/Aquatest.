from standards.models import Standard,WaterUseType
from django.contrib import admin
from hq.models import *
from resources.models import *
from django.contrib import admin


class WaterUseTypeAdmin(admin.ModelAdmin):
    list_display = ('description', 'modified','created')
admin.site.register(WaterUseType, WaterUseTypeAdmin)

class StandardAdmin(admin.ModelAdmin):
    list_display = ('name','govering_body','date_effective','modified','created','water_use_type')
admin.site.register(Standard, StandardAdmin)

