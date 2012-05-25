from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey
from django.core.urlresolvers import reverse

class Tag(models.Model):
	nome = models.CharField(max_length=30, unique=True)
	
	def get_absolute_url(self):
		return reverse('tag', kwargs={'tag_nome': self.nome})
	
	def __unicode__(self):
		return self.nome

class TagItem(models.Model):
	class Meta:
		unique_together = ('tag', 'content_type', 'object_id')
		
	tag = models.ForeignKey(Tag)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField(db_index=True)
	objeto = GenericForeignKey('content_type', 'object_id')
