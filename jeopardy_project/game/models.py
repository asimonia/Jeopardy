from __future__ import unicode_literals

from django.db import models

ROUNDS = [
	(1, 'Jeopardy!'),
	(2, 'Double Jeopardy!'),
	(3, 'Final Jeopardy!'),
	(4, 'Tiebreaker'),
]

# Create your models here.
class Question(models.Model):

	category = models.CharField(max_length=255)
	air_date = models.CharField(max_length=10)
	question = models.TextField()
	value = models.IntegerField()
	answer = models.CharField(max_length=255)
	show_number = models.CharField(max_length=6)
	current_round = models.CharField(max_length=50, choices=ROUNDS)

	def __str__(self):
		return self.question