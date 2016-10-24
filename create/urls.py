from django.conf.urls import url

from . import views

app_name = 'create' #This enables namespacing (eg. using links in templates <a href="{% url mainpage:index'%}")
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.create_new_entry, name='create_new_entry'),
    #url(r'^new', views.create_new_entry, name='create_new_entry'),
]