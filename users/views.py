from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
	"""Faz logout personalizado do usuario"""
	#Esta funçao n esta sendo usada de momento o log out esta sendo feito
	#de forma automatica em url.py 
	logout(request)
	return HttpResponseRedirect("http://127.0.0.1:8000/")


def register(request):
	"""Faz o cadastro de um novo usuário"""
	if request.method != "POST":
		# Exibe o formulario de cadastro em branco
		form = UserCreationForm()
	else:
		# Processa o formulario preenchido
		form = UserCreationForm(data = request.POST)

	if form.is_valid():
		new_user = form.save()
		# Faz login do user e o redirenciona para pangina inicial
		authenticated_user =authenticate(username = new_user.username, password = request.POST["password1"])
		login(request, authenticated_user)
		return HttpResponseRedirect("http://127.0.0.1:8000/")

	context = {"form":form}
	return render(request, "registration/register.html",context)
