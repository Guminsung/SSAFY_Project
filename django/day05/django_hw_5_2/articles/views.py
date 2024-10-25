from django.shortcuts import redirect, render
from .models import Article
# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, "articles/index.html", context)


def new(request):
    return render(request, "articles/new.html")


def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.created_at = request.POST.get('created_at')
    article.updated_at = request.POST.get('updated_at')
    article.save()
    return redirect("articles:index")
