from django.template import Library
from django.contrib.contenttypes.models import ContentType

from tags.models import TagItem

register = Library()

@register.filter
def tags_para_objeto(objeto):
	tipo_dinamico = ContentType.objects.get_for_model(objeto)
	
	itens = TagItem.objects.filter(content_type=tipo_dinamico,
								object_id=objeto.id,
								)

	return [item.tag for item in itens]