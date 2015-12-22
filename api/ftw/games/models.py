from __future__ import unicode_literals

from django.db import models


class Game(models.Model):
	title = models.CharField(max_length=100)
    artwork = models.URLField()
    achievement_count = models.IntegerField()
