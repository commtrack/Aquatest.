from django.db import models

class WaterUseType(models.Model):
    description = models.CharField(max_length=100)
    modified = models.DateTimeField()
    created = models.DateTimeField()

    def __unicode__(self):
        return self.description


class Standard(models.Model):
    name = models.CharField(max_length=50)
    govering_body = models.CharField(max_length=100)
    date_effective = models.DateField()
    modified = models.DateTimeField()
    creted = models.DateTimeField()
    water_use_type = models.ForeignKey(WaterUseType)

    def __unicode__(self):
        return self.name
    


