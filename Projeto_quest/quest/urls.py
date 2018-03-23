from django.conf.urls import url
from quest.views import PerguntasCreate,PerguntasListView, PerguntasDelete,PerguntasUpdate
from . import views

urlpatterns = [
    url(r'register/$', views.register, name='register'),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^criacao/$', views.create_quest, name='criacao'),
    url(r'^perguntas/add/$', PerguntasCreate.as_view() , name='perguntas_add'),
    url(r'^perguntas/$', PerguntasListView.as_view(), name='perguntas'),
    url(r'perguntas/(?P<pk>[0-9]+)/delete/$', PerguntasDelete.as_view(), name='perguntas_delete'),
    url(r'author/(?P<pk>[0-9]+)/$', PerguntasUpdate.as_view(), name='perguntas_update'),
]