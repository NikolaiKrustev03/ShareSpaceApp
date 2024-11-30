from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('edit/', views.UserEditView.as_view(), name='edit'),
    path('profile/', views.user_profile, name='profile'),
    path('delete/', views.delete_user, name='delete'),
    path('logout/', views.logout_view, name='logout'),
]