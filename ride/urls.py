from django.urls import path
from . import views

urlpatterns =[
    path('',views.dashboard, name='dashboard'),
    path('create_ride',views.create_ride, name='create_ride'),
    path('matches',views.matches, name='matches'),
    path('search',views.search, name='search'),
    path('profile',views.profile, name='profile')
]