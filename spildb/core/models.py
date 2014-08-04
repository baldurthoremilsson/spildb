from django.db import models


class Spil(models.Model):
    name = models.CharField(max_length=255)
    score = models.FloatField()
    logo = models.ImageField(upload_to='logos')
    rules = models.FileField(upload_to='rules')
    players_min = models.IntegerField()
    players_max = models.IntegerField(blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        ordering = ('name', 'score')

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return {
                'id': self.id,
                'name': self.name,
                'score': self.score,
                'logo': self.logo.url,
                'rules': self.rules.url,
                'players_min': self.players_min,
                'players_max': self.players_max,
                'parent': self.parent.id if self.parent else None
                }
