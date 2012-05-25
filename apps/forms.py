from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext as _
from django.core.mail import send_mail

class FormRegistro(forms.ModelForm):
    class Meta:
        model = User
	
	fields = ('username', 'first_name', 'last_name', 'email', 'password')
	
	confirme_a_senha = forms.CharField(
		max_length=30, widget=forms.PasswordInput
		)
	
	def __init__(self, *args, **kwargs):
		self.base_fields['password'].help_text = 'Digite uma senha segura'
		self.base_fields['password'].idget=forms.PasswordInput()
		super(FormRegistro, self).__init__(*args, **kwargs)
	
	def clean_username(self):
		if User.objects.filter(
			username=self.cleaned_data['username'],
			).count():
			raise forms.ValidationError('Ja existe um usuario com este username')
			
		return self.cleaned_data['username']

    def clean_email(self):
        if User.objects.filter(
            email=self.cleaned_data['email'],
            ).count():
            raise forms.ValidationError('Ja existe um usuario com este e-mail')

        return self.cleaned_data['email']

    def clean_confirme_a_senha(self):
        if self.cleaned_data['confirme_a_senha'] != self.data['password']:
            raise forms.ValidationError('Confirmacao da senha nao confere!')

        return self.cleaned_data['confirme_a_senha']

    def save(self, commit=True):
        usuario = super(FormRegistro, self).save(commit=False)

        usuario.set_password(self.cleaned_data['password'])

        if commit:
			usuario.save()

        return usuario
		
class FormContato(forms.Form):
	nome = forms.CharField(max_length=50, label=_('Nome'))
	email = forms.EmailField(required=False, label=_('E-mail'))
	mensagem = forms.Field(widget=forms.Textarea, label=_('Mensagem'))
	
	def enviar(self):
		titulo = 'Mensagem automatica pelo site'
		destino = 'paavomsoeiro@gmail.com'
		texto = """
		Nome: %(nome)s
		Email: %(email)s
		Mensagem:
		%(mensagem)s
		""" % self.cleaned_data
		
		send_mail(
			subject=titulo,
			message=texto,
			from_email=destino,
			recipient_list=[destino],
			)