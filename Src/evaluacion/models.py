from django.db import models
from django.utils import formats
from django.core.urlresolvers import reverse
from certificacion.models import *

class Evaluacion(models.Model):
	creacion = models.DateTimeField(auto_now_add=True)
	actualizacion = models.DateTimeField(auto_now=True)
	certificacion = models.ForeignKey(Certificacion)

	def __str__(self):
		return self.certificacion.nombre + ' - ' + str(self.creacion)

	def getNombre(self):
		return self.certificacion.nombre

	def getFecha(self):
		return formats.date_format(self.creacion, "SHORT_DATETIME_FORMAT")

class Calificacion(models.Model):
	control = models.ForeignKey(Control)
	evaluacion = models.ForeignKey('Evaluacion')
	cumplimiento = models.ForeignKey('Cumplimiento', default=1)
	comentario = models.CharField(max_length=1000, null=True, blank=True)
	ejemplo = models.CharField(max_length=1000, null=True, blank=True)

	def __str__(self):
		return self.control.nombre

class Cumplimiento(models.Model):
	titulo = models.CharField(max_length=120, unique=True, null=True, blank=True)

	def __str__(self):
		return self.titulo