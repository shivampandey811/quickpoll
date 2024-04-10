from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_poll, name='create_poll'),
    path('vote/<int:poll_id>/', views.vote, name='vote'),
    path('results/<int:poll_id>/', views.results, name='results'),
]
