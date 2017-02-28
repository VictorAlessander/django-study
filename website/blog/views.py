from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
#from .forms import CadastroForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):

	return render(request, 'index.html')


def cadastro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST or None)

		if form.is_valid():
			form.save()
			return redirect('/')

	else:
		form = UserCreationForm()

	return render(request, 'cadastro.html', {'form': form})


def entrar(request):

	return render(request, 'entrar.html', {})