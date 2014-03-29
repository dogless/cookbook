from django.db import models

# Create your models here.
class Recipe(models.Model):
	name = models.CharField(max_length=255)

class Step(models.Model):
	number = models.IntegerField()
	recipe = models.ForeignKey(Recipe)

	class Meta:
		ordering = ('number',)
