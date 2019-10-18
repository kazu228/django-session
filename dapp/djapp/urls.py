from django.conf.urls import url
from . import views

app_name = 'djapp'

urlpatterns = [
    url('', views.kakikomi, name='kakikomi'),
]
