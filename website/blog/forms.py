from django import forms


class CadastroForm(forms.Form):

	your_name = forms.CharField(label='Name')