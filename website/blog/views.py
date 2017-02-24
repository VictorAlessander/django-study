from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CadastroForm

# Create your views here.


def index(request):

	return render(request, 'index.html')


def cadastro(request):

	if request.method == 'POST':
		form = CadastroForm(request.POST or None)

		if form.is_valid():
			return HttpResponseRedirect('/')

	else:
		form = CadastroForm()

	return render(request, 'cadastro.html', {'form': form})