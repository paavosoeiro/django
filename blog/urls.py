from django.conf.urls.defaults import *
from blog.models import Artigo

info_dict = {
	'queryset': Artigo.objects.all(),
	'date_field': 'publicacao',
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.date_based.archive_index', info_dict),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^artigo/(?P<slug>[\w_-]+)/$', 'blog.views.artigo'),
	
)