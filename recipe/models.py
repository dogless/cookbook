from django.db import models

# Create your models here.
class Recipe(models.Model):
	name = models.CharField(max_length=255)
	avatar = models.ImageField("Recipe Pic", upload_to="images/", blank=True, null=True)

	def __unicode__(self):
		return self.name

class Step(models.Model):
	number = models.IntegerField()
	details = models.CharField(max_length=255)
	avatar = models.ImageField("Step Pic", upload_to="images/", blank=True, null=True)
	recipe = models.ForeignKey(Recipe)

	def __unicode__(self):
		return unicode(self.number)

	class Meta:
		ordering = ('number',)
