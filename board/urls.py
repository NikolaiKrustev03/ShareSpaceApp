from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('create/', views.create_board, name='create_board'),
    path('<int:pk>/', views.board_detail, name='board_detail'),
    path('<int:pk>/edit/', views.edit_board, name='edit_board'),
    path('delete/<int:pk>/', views.delete_board, name='delete_board'),
]
