from smsnotifications.models import SmsNotification
from django.contrib import admin
from hq.models import *

class SmsNotificationAdmin(admin.ModelAdmin):
    list_display = ('sampling_point', 'authorised_sampler', 'notification_type','digest','modified','created')
admin.site.register(SmsNotification,SmsNotificationAdmin)


