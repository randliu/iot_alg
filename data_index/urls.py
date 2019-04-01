from django.conf.urls import url
from data_index import views

app_name = 'data_index'

urlpatterns = [
    url(r'^current_datetime/$',  views.current_datetime, name='current_datetime'),
]

