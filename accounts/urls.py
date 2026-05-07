from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
