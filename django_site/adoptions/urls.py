from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pet_detail/<int:pet_id>/', views.pet_detail, name='pet_detail'),
]
