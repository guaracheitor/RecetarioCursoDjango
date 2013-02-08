# Create your views here.
from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render_to_response('lista_recetas.html',{'recetas':recetas}, context_instance=RequestContext(request))

def sobre(request):
	html = "<html><body>Proyecto de ejemplo de MDW</body></html>"
	return HttpResponse(html)