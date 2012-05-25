from django.template.defaultfilters import slugify

def slug_pre_save(signal, instance, sender, **kwargs):
	if not instance.slug:
		slug = slugify(instance.titulo)
		novo_slug = slug
		contador = 0
		
		while sender.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
			contador += 1
			novo_slug = '%s-%d'%(slug, contador)
		
		instance.slug = novo_slug
