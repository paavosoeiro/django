from datetime import date
from django import forms
from contas.models import ContaPagar, ContaReceber
from django.forms.extras.widgets import SelectDateWidget

class FormPagamento(forms.Form):
	valor = forms.DecimalField(max_digits=15, decimal_places=2)
	
	def salvar_pagamento(self, conta):
		return conta.lancar_pagamento(	
			data_pagamento=date.today(),
			valor=self.cleaned_data['valor'],
			)

class FormContaPagar(forms.ModelForm):
	class Meta:
		model = ContaPagar
	
		exclude = ('usuario', 'operacao', 'data_pagamento')
	
	def __init__(self, *args, **kwargs):
		self.base_fields['data_vencimento'].widget = SelectDateWidget()
		
		super(FormContaPagar, self).__init__(*args, **kwargs)

class FormContaReceber(forms.ModelForm):
	class Meta:
		model = ContaReceber
	
		exclude = ('usuario', 'operacao', 'data_pagamento')
	
	def __init__(self, *args, **kwargs):
		self.base_fields['data_vencimento'].widget = SelectDateWidget()
		
		super(FormContaReceber, self).__init__(*args, **kwargs)