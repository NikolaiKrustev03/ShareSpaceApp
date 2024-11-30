from django.urls import path
from .views import CommentView, comment_delete

app_name = 'comment'

urlpatterns = [
    path('add/<int:pk>/', CommentView.as_view(), name='add_comment'),
    path('delete/<int:pk>/', comment_delete, name='comment_delete')

]
