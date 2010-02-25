from django.db import models
from hq.models import ExtUser
from locations.models import Location
from datetime import datetime
from standards.models import Standard, WaterUseType

# Create your Django models here, if you need them.
class Sample(models.Model):
    '''
    This is sample
    '''
    taken_by = models.ForeignKey(ExtUser)
    sampling_point = models.ForeignKey(Location)
    notes = models.TextField()
    date_taken = models.DateTimeField()
    date_received = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def __unicode__(self):
        return self.notes

class Parameter(models.Model):
    test_name = models.CharField(max_length=120)
    unit = models.CharField(max_length=50)
    lookup_hint = models.BooleanField()
    test_name_short = models.CharField(max_length=20)
    modifed = models.DateTimeField()

class MeasuredValue(models.Model):
    '''
    The measured values
    '''
    sample = models.ForeignKey(Sample)
    parameter = models.ForeignKey(Parameter)
    value = models.IntegerField()
    modified = models.DateTimeField()
    created = models.DateTimeField()

class ValueRule(models.Model):
    '''
    Rules Applied to the values
    '''
    description = models.TextField()
    parameter = models.ForeignKey(Parameter)
    standard = models.ForeignKey(Standard)
    water_use_type = models.ForeignKey(WaterUseType)
    modified = models.DateTimeField()
    created = models.DateTimeField()

class NormalRange(models.Model):
    '''
    Normal range for values.
    '''
    description = models.CharField(max_length=200)
    value_rule = models.ForeignKey(ValueRule)
    maximum = models.IntegerField()
    minimum = models.IntegerField()
    modified = models.DateTimeField()
    created = models.DateTimeField()

class AbnormalRange(models.Model):
    description = models.CharField(max_length=200)
    value_rule = models.ForeignKey(ValueRule)
    maximum = models.IntegerField()
    minimum = models.IntegerField()
    remedialaction = models.CharField(max_length=20)
    color = models.CharField(max_length=25)
    modified = models.DateTimeField()
    created = models.DateTimeField()

    