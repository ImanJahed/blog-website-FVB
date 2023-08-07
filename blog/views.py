from django.shortcuts import get_object_or_404, render

from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all()

    context = {'articles': articles}
    return render(request, 'blog/article_list.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug_article=slug)

    context = {'article': article}
    return render(request, 'blog/article_detail.html', context)