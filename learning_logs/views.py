from django.shortcuts import render
from .models import Topic

def index(request):
	"""A pagina inicial de learning Log"""
	return render(request,"learning_logs/index.html")

def topics(request):
	"""Mostra todos assuntos"""
	topics = Topic.objects.order_by("date_added")
	context = {"topics":topics}
	return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
	"""Mostra um unico assunto e suas entradas"""
	topic = Topic.objects.get(id = topic_id)
	entries = topic.entry_set.order_by("-date_added")
	context = {"topic" : topic, "entries":entries}
	return render(request,"learning_logs/topic.html",context)
