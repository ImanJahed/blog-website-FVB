from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.user_register, name='signup'),
    # path('edit/', views.user_edit, name='edit'),
    path('edit/', views.user_edit_model, name='edit'),
]
