from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'views.index'),
	(r'^polls/', include('polls.urls')),
	(r'^blog/', include('blog.urls')),
	(r'^contato/$', 'views.contato'),
	(r'^galeria/', include('galeria.urls')),
	(r'^tags/', include('tags.urls')),
	(r'^i18n/', include('django.conf.urls.i18n')),
	(r'^contas/', include('contas.urls')),
	(r'^entrar/$', 'django.contrib.auth.views.login',
        {'template_name': 'entrar.html'}, 'entrar'),
    (r'^sair/$', 'django.contrib.auth.views.logout',
        {'template_name': 'sair.html'}, 'sair'),
    (r'^registrar/$', 'views.registrar', {}, 'registrar'),
	(r'^todos_os_usuarios/$', 'views.todos_os_usuarios',
		{}, 'todos_os_usuarios'),
	(r'^mudar_senha/$', 'django.contrib.auth.views.password_change',
		{'template_name': 'mudar_senha.html'}, 'mudar_senha'),
	(r'^mudar_senha/concluido/$', 'django.contrib.auth.views.password_change_done',
		{'template_name': 'mudar_senha_concluido.html'}, 'mudar_senha_concluido'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.LOCAL:
	urlpatterns += patterns('',
		(r'^media/(.*)$', 'django.views.static.serve', 
			{'document_root': settings.MEDIA_ROOT}),
	)