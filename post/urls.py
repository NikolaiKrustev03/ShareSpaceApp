from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('explore/', views.post_list, name='post_list'),
    path('<int:pk>/save_to_board/', views.save_to_board, name='save_to_board'),
    path('<int:pk>/toggle_like/', views.toggle_like, name='toggle_like'),
]
