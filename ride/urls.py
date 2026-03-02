from django.urls import path
from . import views

urlpatterns =[
    path('',views.dashboard, name='dashboard'),
    path('create_ride',views.create_ride, name='create_ride')
]