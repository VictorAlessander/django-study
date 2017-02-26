from django.db import models


# Create your models here.


class Cadastro(models.Model):

	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	username = models.CharField(max_length=40)
	password = models.CharField(max_length=50)