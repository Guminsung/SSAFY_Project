from django.shortcuts import render, redirect
from .models import Diary
from .forms import CommentForm, DiaryForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comment_form = CommentForm()
    comments = [diary.comment_set.all() for diary in diaries]
    context = {
        'diaries': diaries,
        'comment_form' : comment_form,
        'commnets' : comments,
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comment_create(request, pk):
    diary = Diary.objects.get(pk = pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.diary = diary
        comment_form.save()
        return redirect('diaries:index')
    context = {
        'diary':diary,
        'comment_form' : comment_form,
    }
    return render(request, 'diaries/index.html', context)