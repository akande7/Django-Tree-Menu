from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="main_menu"),
    path('mens1/', views.men1, name="mens1"),
    path('mens2/', views.men2, name="mens2"),
    path('sale/', views.sale, name="sale"),
    path('sale1/', views.sale1, name="sale1"),
    path('sale2/', views.sale2, name="sale2"),
    path('womens/', views.womens, name="womens"),
    path('womens1/', views.women1, name="womens1"),
    path('mens/', views.mens, name="men"),
    
    
]