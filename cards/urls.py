from django.urls import path
from cards import views

urlpatterns = [
    path('cards', views.cards_list),
    path('cards/', views.cards_list),
    path('cards/<int:pk>/', views.cards_detail),
    path('cards/<int:pk>', views.cards_detail),
]