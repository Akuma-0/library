from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/',views.user_login),
    path('logout/',views.user_logout),
path('edit-profile/', views.edit_profile, name='edit_profile'),
path('profile/', views.user_profile, name='user_profile'),
]