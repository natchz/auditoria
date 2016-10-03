from django.shortcuts import render, redirect
from muro.models import Trabajo, Estado
from certificacion.models import Certificacion, Control
from evaluacion.models import Evaluacion, Calificacion

#Funcion para tomar un trabajo
def tomar(request, id):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')

	trabajo = Trabajo.objects.get(id=id)
	trabajo.auditor = usuario
	trabajo.estado = Estado.objects.get(titulo='Activo')
	trabajo.save() 

	return redirect('usuario:inicio')

#Vista para ver trabajos inactivos
def lista(request):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')

	trabajos = Trabajo.objects.filter(estado__titulo='Inactivo').order_by('-creacion')
	datos = {
		'trabajos': trabajos,
	}

	return render(request, 'lista.html', datos)

#Vista para crear trabajos
def crear(request):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')

	certificaciones = Certificacion.objects.all()

	datos = {
		'certificaciones': certificaciones,
	}

	return render(request, 'crear_trabajo.html', datos)

#Funcion para crear un trabajo
def crear_post(request):
	usuario = request.user
	if not usuario.is_authenticated():
		return redirect('raiz:inicio')

	certificacion = Certificacion.objects.get(id=request.POST['certificacion'])
	evaluacion = Evaluacion.objects.create(certificacion=certificacion)

	estado = Estado.objects.get(titulo='Inactivo')

	Trabajo.objects.create(empresa=usuario, evaluacion=evaluacion, estado=estado)

	controles = Control.objects.filter(objetivo__dominio__certificacion=certificacion)
	for control in controles:
		Calificacion.objects.create(control=control, evaluacion=evaluacion)

	return redirect('usuario:inicio')