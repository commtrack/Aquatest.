from django.db import models
from reporters.models import Reporter
from wqm.models import SamplingPoint
from datetime import datetime

class SmsNotification(models.Model):
    sampling_point = models.ForeignKey(SamplingPoint)
    authorised_sampler = models.ForeignKey(Reporter)
    notification_type = models.CharField(max_length=50)
    digest = models.BooleanField()
    modified = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(default=datetime.now())


def __unicode__(self):
        return self.notification_type
