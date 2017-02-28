from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

# Create your views here.


def index(request):
	lista_posts = Post.objects.all().order_by('-id')
	return render(request, 'index.html', {'lista_posts': lista_posts})


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


def novo_post(request):

	if request.method == 'POST':
		form_post = PostForm(request.POST)

		if form_post.is_valid():
			post = form_post.save(commit=False)
			post.author = request.user
			post.date_created = timezone.now()
			post.save()
			return redirect('/')

	else:
		form_post = PostForm()

	return render(request, 'novo_post.html', {'form_post': form_post})