import datetime

from django.contrib.auth.models import User
from contas.models import Conta, CONTA_STATUS_APAGAR

def obter_contas_pendentes(usuario, prazo_dias):
	delta = datetime.timedelta(days=prazo_dias)
	
	return Conta.objects.filter(
		usuario=usuario,
		status=CONTA_STATUS_APAGAR,
		data_vencimento__lte=datetime.date.today() + delta
		)
		
def enviar_contas_pendentes(usuario, prazo_dias):
	contas_pendentes = obter_contas_pendentes(usuario, prazo_dias)
	
	if not contas_pendentes.count():
		return False
	
	texto = """
	Voce tem as seguintes contas vencidas ou a vencer nos proximo %(dias)d dias:
	
	%(lista_de_contas)s
	"""%{
		'dias': prazo_dias,
		'lista_de_contas': "\n".join([unicode(conta) for conta in contas_pendentes]),
		}
	
	return usuario.email_user(
		'Contas a pagar e receber',
		texto,
		)
		
from django.core.mail import send_mail
import urllib2

def obter_status_code(url):
	try:
		urllib2.urlopen(url)
	except urllib2.HTTPError, e:
		return e.code
	except Exception:
		return 0
	
	return 200

def verificar_pagina_inicial(funcao_status_code=obter_status_code,
	url='http://localhost:8000/blog/'):
	status_code = funcao_status_code(url)
	
	if status_code != 200:
		send_mail(
			'Erro na pagina inicial',
			'Ocorreu um erro no site, verifique!',
			'paavomsoeiro@gmail.com',
			['paavomsoeiro@gmail.com'],
			)
	
	return True