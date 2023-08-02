from django.urls import path
from . import views

urlpatterns = [
    path('send_mssg', views.SendPushNotitification.as_view() , name='send_mssg'),
]
