from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'), 
    path('email_send/<str:mailss>/', views.email_send, name='email_send'),
    path('login/', views.login, name='login'),
    path('home/',views.home,name='home'),
]