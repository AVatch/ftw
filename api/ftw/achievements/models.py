from __future__ import unicode_literals

from django.db import models

from games.models import Game


class Achievement(models.Model):
	title = models.CharField(max_length=100)
	game = models.ForeignKey(Game)
    artwork = models.URLField()
    points = models.IntegerField()
    description = models.TextField()
