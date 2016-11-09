from django.conf.urls import url

from . import views

app_name = 'create' #This enables namespacing (eg. using links in templates <a href="{% url mainpage:index'%}")
urlpatterns = [
    url(r'^$', views.show_forms, name='show_forms'),
    url(r'^event$', views.create_new_event, name='create_new_event'),
    url(r'^class$', views.create_new_class, name='create_new_class'),
    #url(r'^new', views.create_new_entry, name='create_new_entry'),
]