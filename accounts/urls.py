from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/registration/', views.RegisterView.as_view(), name='registration'),
    path('accounts/authorization/', views.LoginView.as_view(), name='authorization'),
    path('logout/', views.user_logout, name='user_logout')
]
