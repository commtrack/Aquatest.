from standards.models import Standard,WaterUseType


from django.contrib import admin

#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']

#admin.site.register(Poll, PollAdmin)

admin.site.register(Standard)
admin.site.register(WaterUseType)

