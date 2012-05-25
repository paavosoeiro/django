from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from tags.models import Tag

def tags(request):
	lista = Tag.objects.all()
	return render_to_response('tags/tags.html', 
							locals(),
							context_instance=RequestContext(request),
							)
							
def tag(request, tag_nome):
	tag = get_object_or_404(Tag, nome=tag_nome)
	
	return render_to_response('tags/tag.html',
							locals(),
							context_instance=RequestContext(request),
							)