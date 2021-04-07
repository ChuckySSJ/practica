from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context

# Create your views here.

def josemanuel(request):
		externo = open("C:/Users/Chucky/Desktop/josemanuellopez/josemanuel/templates/index.html")
		plantilla = Template(externo.read())
		externo.close()
		ctx = Context()
		contenido = plantilla.render(ctx)
		return HttpResponse(contenido)