from django.db import models


class Like(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on {self.post.title}"
