from django.contrib import admin
from samples.models import *

class SampleAdmin(admin.ModelAdmin):
    list_display = ('taken_by','sampling_point','notes','date_taken','date_received','created','modified')
admin.site.register(Sample, SampleAdmin)

class ParameterAdmin(admin.ModelAdmin):
    list_display = ('test_name','unit','lookup_hint','test_name_short','modifed')
#    list_filter = ['']
    search_fields = ('test_name','unit','lookup_hint','test_name_short','modifed')
admin.site.register(Parameter, ParameterAdmin)

admin.site.register(MeasuredValue)
admin.site.register(ValueRule)
admin.site.register(NormalRange)
admin.site.register(AbnormalRange)