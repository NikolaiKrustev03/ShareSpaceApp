from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.http import HttpResponseForbidden
from post.models import Post
from .models import Comment
from .forms import CommentForm


class CommentView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if not request.user.is_authenticated:
            return HttpResponseForbidden("You must be logged in to comment.")

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():

            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

            return redirect('post:post_detail', pk=post.pk)
        else:
            comments = post.comments.all()
            return render(request, 'post/post_detail.html', {
                'post': post,
                'comments': comments,
                'comment_form': comment_form,
            })


def comment_delete(request, pk):

    comment = get_object_or_404(Comment, pk=pk)

    post = comment.post

    if comment.user == request.user or request.user.is_staff:
        comment.delete()

        return redirect('post:post_detail', pk=post.pk)

    return HttpResponseForbidden("You are not authorized to delete this comment.")