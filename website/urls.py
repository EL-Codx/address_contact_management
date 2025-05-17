from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/<int:pk>', views.single_contact, name='single_contact'),
    path('about/', views.about, name='about'),
    path('delete/<int:pk>', views.delete_contact, name='delete'),
    path('add_contact', views.add_contact, name='add_contact'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register_user'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('change_password/', views.change_password, name='change_password')
]
