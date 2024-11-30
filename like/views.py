from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from common.utils import get_post_model
from .models import Like


Post = get_post_model()


def toggle_like(request, pk):
    post = get_object_or_404(get_post_model(), pk=pk)

    if request.user.is_authenticated:
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
        return redirect('post:post_detail', pk=post.pk)
    else:
        raise Http404("You must be logged in to like a post.")
