from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import Artigo

def artigo(request, slug):
	artigo = get_object_or_404(Artigo, slug=slug)
	return render_to_response('blog/artigo.html', locals(),
		context_instance=RequestContext(request),
		)