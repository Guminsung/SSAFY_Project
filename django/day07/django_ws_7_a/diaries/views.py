from django.shortcuts import redirect, render
from diaries.forms import DiaryForm
from diaries.models import Diary

# Create your views here.


def index(request):
    diaries = Diary.objects.all()
    context = {
        'diaries': diaries,
    }
    return render(request, 'diaries/index.html', context)


def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form,
    }
    return render(request, 'diaries/create.html', context)
