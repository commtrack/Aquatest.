from django.contrib import admin
from samples.models import *


#class ResourceAdmin(admin.ModelAdmin):
#    list_display = ('name', 'code', 'category','domain')
#    list_filter = ['domain', 'category', 'status']
#    search_fields = ('name','code')
#admin.site.register(Resource,ResourceAdmin)

admin.site.register(Sample)
admin.site.register(Parameter)
admin.site.register(MeasuredValue)
admin.site.register(ValueRule)
admin.site.register(NormalRange)
admin.site.register(AbnormalRange)