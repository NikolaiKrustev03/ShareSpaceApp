from django.db import models


class Post(models.Model):
    TAG_CHOICES = [
        ('diy', 'DIY'),
        ('life', 'Life'),
        ('photography', 'Photography'),
        ('travel', 'Travel'),
        ('tech', 'Tech'),
        ('food', 'Food'),
    ]

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='posts')
    boards = models.ManyToManyField('board.Board', related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    tag = models.CharField(
        max_length=50,
        choices=TAG_CHOICES,
        default='LIFE',
    )
    image1 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
