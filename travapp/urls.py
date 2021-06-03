from django.urls import path
from travapp import views
urlpatterns = [
    path('', views.index),
]
