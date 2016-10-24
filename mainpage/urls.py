from django.conf.urls import url

from . import views

#This enables namespacing (eg. using links in 
#templates <a href="{% url mainpage:index'%}")
app_name = 'mainpage'
urlpatterns = [
    url(r'^$', views.main_view_not_logged_in, name='main_view_not_logged_in'), #name enables using links?
    url(r'^$', views.main_view_logged_in, name='main_view_logged_in'),
    #url(r'^test', views.test, name='test'), #MOVED TO SCHEDULE
]