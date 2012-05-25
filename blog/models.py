from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import signals
from datetime import datetime
from utils.signals_comuns import slug_pre_save


class Artigo(models.Model):
	class Meta:
		ordering = ('-publicacao',)

	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	publicacao = models.DateTimeField(default=datetime.now(), blank=True)
	slug = models.SlugField(max_length=100, blank=True, unique=True)
	
	def get_absolute_url(self):
		return reverse('blog.views.artigo', kwargs={'slug': self.slug})
	
	def __unicode__(self):
		return self.titulo

signals.pre_save.connect(slug_pre_save, sender=Artigo)