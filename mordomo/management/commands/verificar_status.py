from django.core.management import BaseCommand
from mordomo.models import verificar_pagina_inicial
from optparse import make_option
from django.conf import settings

class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
		make_option('--url',
					default='/',
					dest='url',
					help='Informe a URL para verificar o status',
					),
		)
	help = 'Verifica uma URL e envia email ao admin de estiver com erro'
	requires_model_validation = True
	
	def handle(self, url, **kwargs):
		url = settings.PROJECT_ROOT_URL[:-1] + url
		verificar_pagina_inicial(url=url)
		print 'URL "%s" verificada'%url