from django.conf.urls import url
from quest.views import PerguntasCreate
from . import views

urlpatterns = [
    url(r'register/$', views.register, name='register'),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^criacao/$', views.create_quest, name='criacao'),
    url(r'^perguntas/add/$', PerguntasCreate.as_view() , name='perguntas_add'),
]