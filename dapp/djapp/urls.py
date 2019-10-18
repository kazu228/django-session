from django.urls import path
from . import views

app_name = 'djapp'

urlpatterns = [
    path('', views.kakikomi, name='kakikomi'),
    path('user_data_confirm/', views.user_data_confirm, name='user_data_confirm'),
]
