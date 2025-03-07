from django.http import HttpResponseRedirect, Http404
#from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

def index(request):
	"""A pagina inicial de learning Log"""
	return render(request,"learning_logs/index.html")

@login_required
def topics(request):
	"""Mostra todos assuntos"""
	topics = Topic.objects.filter(owner = request.user).order_by("date_added")
	context = {"topics":topics}
	return render(request, "learning_logs/topics.html", context)

@login_required
def topic(request, topic_id):
	"""Mostra um unico assunto e suas entradas"""
	topic = Topic.objects.get(id = topic_id)
	# Garante que o assunto pertence ao usuario atual
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by("-date_added")
	context = {"topic" : topic, "entries":entries}
	return render(request,"learning_logs/topic.html",context)

@login_required
def new_topic(request):
	"""Adciona um novo assunto"""
	if request.method != "POST":
		#Nenhum dado submetido cria um formulario em branco
		form = TopicForm()
	else:
		#Dados do POST submetidos processa os dados
		form = TopicForm(request.POST)

	if form.is_valid():
		new_topic = form.save(commit = False)
		new_topic.owner = request.user
		new_topic.save()
		#return HttpResponseRedirect(reverse("learning_logs:topics"))
# O reverse determina o url a partir de um padrão de URL nomeado, mas parece
# que já ñ é assim que se faz depois vejo como fazer ...
		return HttpResponseRedirect("http://127.0.0.1:8000/topics")
	context = {"form" : form}
	return render(request,"learning_logs/new_topic.html",context)

@login_required
def new_entry(request, topic_id):
	"""Acrescenta uma nova entrada para um assunto em particular"""
	topic = Topic.objects.get(id = topic_id)
	if topic.owner != request.user:
		raise Http404
	if request.method != "POST":
		#Nenhum dado submetido Cria um formulario vazio
		form = EntryForm()
	else:
		#Dados de POST submetidos processa os dados
		form = EntryForm(data=request.POST)

	if form.is_valid():
		new_entry = form.save(commit = False)
		new_entry.topic = topic
		new_entry.save()
		args = topic_id
		return HttpResponseRedirect("http://127.0.0.1:8000/topic/"+str(args))
#Onde esta o links seria reverse("learning_logs:topic",args=[topic_id])
#Mas como disse o reverse esta em desatualizao
	context = {"topic" : topic, "form" : form}
	return render(request,"learning_logs/new_entry.html",context)

@login_required
def edit_entry(request,entry_id):
	"""Edita uma entrada existente"""
	entry = Entry.objects.get(id = entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != "POST":
		#Requisição inicial preenche previamente o formulario com a entrada actual
		form = EntryForm(instance = entry)
	else:
		#Dados do POST submetidos processa os dados
		form = EntryForm(instance = entry, data = request.POST)

	if form.is_valid():
		form.save()
		args = topic.id
		return HttpResponseRedirect("http://127.0.0.1:8000/topic/"+str(args))

	context = {"entry" : entry, "topic" : topic, "form" : form}
	return render(request,"learning_logs/edit_entry.html",context)
