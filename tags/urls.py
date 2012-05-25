from django.conf.urls.defaults import *

urlpatterns = patterns('tags.views',
	url(r'^$', 'tags', name='tags'),
	url(r'^(?P<tag_nome>.*?)/$', 'tag', name='tag'),
)