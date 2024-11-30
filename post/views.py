from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import Http404
from .forms import PostForm, PostEditForm
from .models import Post
from common.utils import get_comment_form, get_board_model, get_like_model


class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'post/post_create.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post:post_list')
        return render(request, 'post/post_create.html', {'form': form})


class PostEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.user != request.user:
            raise Http404("You are not authorized to edit this post.")

        form = PostEditForm(instance=post)
        return render(request, 'post/post_edit.html', {'form': form, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if post.user != request.user:
            raise Http404("You are not authorized to edit this post.")

        form = PostEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post:post_detail', pk=post.pk)
        return render(request, 'post/post_edit.html', {'form': form, 'post': post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.user == request.user:
        post.delete()
        return redirect('post:post_list')

    if hasattr(request.user, 'is_admin') and request.user.is_staff:
        post.delete()
        return redirect('post:post_list')

    raise PermissionDenied("You are not authorized to delete this post.")


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


CommentForm = get_comment_form()

Board = get_board_model()

Like = get_like_model()


@login_required
def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    existing_like = get_like_model().objects.filter(post=post, user=request.user).first()

    if existing_like:

        existing_like.delete()
    else:

        get_like_model().objects.create(post=post, user=request.user)

    return redirect('post:post_detail', pk=post.pk)


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()

        comment_form = get_comment_form()

        boards = get_board_model().objects.all()

        is_owner = post.user == request.user if request.user.is_authenticated else False

        has_liked = False
        if request.user.is_authenticated:
            has_liked = get_like_model().objects.filter(post=post, user=request.user).exists()

        return render(request, 'post/post_detail.html', {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'is_owner': is_owner,
            'boards': boards,
            'has_liked': has_liked
        })

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comment_form = get_comment_form()(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post:post_detail', pk=post.pk)

        comments = post.comments.all()
        return render(request, 'post/post_detail.html', {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'is_owner': post.user == request.user
        })


def save_to_board(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if not request.user.is_authenticated:
        return redirect('user:login')

    user_boards = get_board_model().objects.filter(user=request.user)

    if request.method == 'POST':
        selected_boards = request.POST.getlist('boards')

        selected_user_boards = user_boards.filter(pk__in=selected_boards)

        if not selected_user_boards.exists() and selected_boards:
            raise Http404("Selected boards do not exist or you do not own them.")

        post.boards.set(selected_user_boards)
        return redirect('post:post_detail', pk=post.pk)

    return render(request, 'post/post_detail.html', {'post': post, 'boards': user_boards})
