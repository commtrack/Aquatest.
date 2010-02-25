from django.db import models

class WqmAuthority(models.Model):
    name = models.CharField(max_length=50)
    modified = models.DateTimeField()
    created = models.DateTimeField()

    def __unicode__(self):
        return self.name

class WqmArea(models.Model):
    name = models.CharField(max_length=50)
    wqmauthority = models.ForeignKey(WqmAuthority)
    modified = models.DateTimeField()
    craeted = models.DateTimeField()

    def __unicode__(self):
        return self.name



