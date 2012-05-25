from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django import forms
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

from forms import FormRegistro, FormContato

def index(request):
	return render_to_response('index.html',
		context_instance=RequestContext(request),
		)

def contato(request):
	if request.method == 'POST':
		form = FormContato(request.POST)
		if form.is_valid():
			form.enviar()
			mostrar = 'Contato enviado!'
	else:
		form = FormContato()
	return render_to_response('contato.html',
		locals(),
		context_instance=RequestContext(request),
		)
#mover esta view para pasta de projeto		
def registrar(request):
	if request.method == 'POST':
		form = FormRegistro(request.POST)
		
		if form.is_valid():
			novo_usuario = form.save()
			return HttpResponseRedirect('/')
	else:
		form = FormRegistro()

	return render_to_response(
		'registrar.html',
		locals(),
		context_instance=RequestContext(request),
		)
		
#mover para pasta de projeto
@permission_required('ver_todos_os_usuarios')
def todos_os_usuarios(request):
	usuarios = User.objects.all()
	return render_to_response(
		'todos_os_usuarios.html',
		locals(),
		context_instance=RequestContext(request),
		)
		