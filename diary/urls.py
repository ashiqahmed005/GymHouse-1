from django.conf.urls import url

from . import views

app_name = 'diary' #This enables namespacing (eg. using links in templates <a href="{% url mainpage:index'%}")
urlpatterns = [
    url(r'^$', views.index, name='index'),
]