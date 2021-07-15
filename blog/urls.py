from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-hmae'),
     path('about/', views.about, name='blog-about'),

]