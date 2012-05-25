try:
	import Image
except ImportError:
	from PIL import Image

from django import forms
from django.contrib import admin

from galeria.models import Album, Imagem
from tags import aplicar_tags, tags_para_objeto

class FormImagem(forms.ModelForm):
	class Meta:
		model = Imagem
		
	tags = forms.CharField(max_length=30, required=False)
	
	def __init__(self, *args, **kwargs):
		super(FormImagem, self).__init__(*args, **kwargs)
		
		if self.instance.id:
			self.initial['tags'] = tags_para_objeto(self.instance)
			
class AdminAlbum(admin.ModelAdmin):
	list_display = ('titulo',)
	search_fields = ('titulo',)
	
class AdminImagem(admin.ModelAdmin):
	list_display = ('album', 'titulo',)
	list_filter = ('album',)
	search_fields = ('titulo', 'descricao',)
	form = FormImagem
	
	def save_model(self, request, obj, form, change):
		super(AdminImagem, self).save_model(request, obj, form, change)
		
		if 'original' in form.changed_data:
			extensao = obj.original.name.split('.')[-1]
			obj.thumbnail = 'galeria/thumbnail/%d.%s'%(obj.id, extensao)
			
			miniatura = Image.open(obj.original.path)
			miniatura.thumbnail((100,100), Image.ANTIALIAS)
			miniatura.save(obj.thumbnail.path)
			
			obj.save()
	
		aplicar_tags(obj, form.cleaned_data['tags'])
		
admin.site.register(Album, AdminAlbum)
admin.site.register(Imagem, AdminImagem)