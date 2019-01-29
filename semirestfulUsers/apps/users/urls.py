from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'new/$', views.new,name='new'),
    url(r'(?P<id>\d+)/show$',views.show,name='show'),
    url(r'create/$', views.create,name='create'),
    url(r'(?P<id>\d+)/delete/$',views.delete,name='delete'),
    url(r'(?P<id>\d+)/edit$',views.edit,name='edit'),
    url(r'(?P<id>\d+)/update/$', views.update,name='update'),
]