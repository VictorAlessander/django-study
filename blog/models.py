from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):

	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	date_created = models.DateTimeField(
					default=timezone.now)
	date_modified = models.DateTimeField(
					blank=True, null=True)
	image = models.ImageField(upload_to='blog', null=True)


	def publicar(self):
		self.date_modified = timezone.now()
		self.save()

	def __str__(self):
		return self.title