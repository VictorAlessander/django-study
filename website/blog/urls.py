from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^cadastro/', views.cadastro, name='cadastrar'),
]