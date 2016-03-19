from django.db import models

class Usuario(models.Model):
	username = models.CharField(max_length=15, primary_key=True)
	password = models.CharField(max_length=15)
	tipoUsuario = models.IntegerField()
