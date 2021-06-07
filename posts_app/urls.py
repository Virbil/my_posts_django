from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts),
    path('add-post', views.add_post),
]