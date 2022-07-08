from django.urls import path

from foods import views

urlpatterns = [
    path('menu/', views.index),
    path('menu/<int:pk>', views.food_detail),
]