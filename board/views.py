from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import BoardForm
from .models import Board


@login_required
def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('board:board_detail', pk=board.pk)
    else:
        form = BoardForm()

    return render(request, 'board/board_create.html', {
        'form': form,
    })




def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    posts = board.posts.all()

    return render(request, 'board/board_detail.html', {
        'board': board,
        'posts': posts,
    })


@login_required()
def board_list(request):
    boards = Board.objects.filter(user=request.user)
    return render(request, 'board/board_list.html', {'boards': boards})

def delete_board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user == board.user:
        board.delete()
        return redirect('board:board_list')
    else:
        return HttpResponse("You are not authorized to delete this board.", status=403)


def edit_board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user != board.user:  # Only allow the board owner to edit
        return HttpResponse("You are not authorized to edit this board.", status=403)

    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('board:board_detail', pk=board.pk)
    else:
        form = BoardForm(instance=board)

    return render(request, 'board/board_edit.html', {'form': form, 'board': board})
