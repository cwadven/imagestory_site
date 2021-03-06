from django.shortcuts import render, redirect
from .models import Category
from board.models import Board
from .forms import Categoryform
from django.db.models import Count
from django.db.models import Case, When

# Create your views here.
def show_category(request):
    categoryform = Categoryform()
    # 게시판에 얼마나 많은 게시글들이 존재하는지 확인하기 위해서 root인 녀석들만 보이게 만들기
    # 비공개는 안 보이도록 설정
    all_category = Category.objects.annotate(board_count=Count(Case(
            When(
                board__post__isnull=True, board__secure='public',
                then='board'
            ),
        ))).all()
    new_boards = Board.objects.filter(post_root__isnull=True).exclude(thumbnail_image='').order_by('-created_at')[:6]
    return render(request, "home.html", {"all_category":all_category,"categoryform":categoryform, "new_boards":new_boards,})

def make_category(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            categoryform = Categoryform(request.POST)
            if categoryform.is_valid():
                categoryform.save()
                return redirect('/')
            else:
                return redirect('/')
    else:
        return redirect('/')

def mod_category(request, id):
    category = Category.objects.get(id=id)
    categoryform = Categoryform(instance=category)
    if request.user.is_superuser:
        if request.method == 'POST':
            categoryform = Categoryform(request.POST, instance=category)
            categoryform.save()
            return redirect('/')
        return render(request, "mod_category.html", {"categoryform":categoryform, "category":category,})
    else:
        return redirect('/')

def del_category(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            category = Category.objects.get(id=id)
            category.delete()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')