from django.urls import path
from . import views

app_name = 'djapp'

urlpatterns = [
    path('', views.kakikomi, name='kakikomi'),
]
