from django.contrib import admin
from django.urls import path
from quest import views
from django.conf.urls import url,include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'quest/', include('quest.urls')),
]
