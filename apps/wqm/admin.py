from wqm.models import WqmAuthority,WqmArea
from django.contrib import admin

#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']

#admin.site.register(Poll, PollAdmin)



#class WqmAuthorityAdmin(admin.ModelAdmin):
#    fields = ['name', 'created', 'modified']
#admin.site.register(WqmAuthority,WqmAuthorityAdmin)

admin.site.register(WqmArea)
admin.site.register(WqmAuthority)

