from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index),
    url('add_words/',views.add),
]