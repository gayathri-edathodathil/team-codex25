from django.urls import path
from . import views

urlpatterns =[
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('admin',views.admin,name='admin'),
    path('profile',views.profile,name='profile'),
    path('budget',views.budget,name='budget'),
]