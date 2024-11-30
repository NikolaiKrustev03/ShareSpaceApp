from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<int:pk>/like/', views.toggle_like, name='toggle_like'),

]