from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
#from django.views.generic.edit import CreateView
#from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^cadastro/', views.cadastro, name='cadastro'),
	url(r'^entrar/', login, name='entrar', kwargs={'template_name': 'entrar.html'}),
	url(r'^sair/', logout, name='sair', kwargs={'template_name': 'index.html'}),
	url(r'^novo_post/', views.novo_post, name='novo_post'),
]