from django.db import models
from datetime import datetime
from django.db.models import signals
from utils.signals_comuns import slug_pre_save
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy

class Album(models.Model):
	class Meta:
		ordering = ('titulo',)
		
	titulo = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, blank=True, unique=True)

	def __unicode__(self):
		return self.titulo
		
	def get_absolute_url(self):
		return reverse('album', kwargs={'slug': self.slug})

class Imagem(models.Model):
	class Meta:
		ordering = ('album', 'titulo',)
		
		verbose_name = ugettext_lazy('Imagem')
		verbose_name_plural = ugettext_lazy('Imagens')

	album = models.ForeignKey(Album)
	titulo = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, blank=True, unique=True)
	descricao = models.TextField(blank=True)
	original = models.ImageField(
		null=True,
		blank=True,
		upload_to='galeria/original',
		)
	thumbnail = models.ImageField(
		null=True,
		blank=True,
		upload_to='galeria/thumbnail',
		)
	publicacao = models.DateTimeField(default=datetime.now, blank=True)
	
	def __unicode__(self):
		return self.titulo
		
	def get_absolute_url(self):
		return reverse('imagem', kwargs={'slug': self.slug})
		
signals.pre_save.connect(slug_pre_save, sender=Album)
signals.pre_save.connect(slug_pre_save, sender=Imagem)