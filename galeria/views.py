from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from galeria.models import Album, Imagem

def albuns(request):
	lista = Album.objects.all()
	return render_to_response('galeria/albuns.html', 
							locals(), 
							context_instance=RequestContext(request),
							)
							
def album(request, slug):
	album = get_object_or_404(Album, slug=slug)
	imagens = Imagem.objects.filter(album=album)
	
	return render_to_response('galeria/album.html',
							locals(),
							context_instance=RequestContext(request),
							)
							
def imagem(request, slug):
	imagem = get_object_or_404(Imagem, slug=slug)
	return render_to_response('galeria/imagem.html',
							locals(),
							context_instance=RequestContext(request),
							)