from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article, Category

# Create your views here.
def article_list(request, cat=None):
    context = {}
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    try:
        page_object = paginator.get_page(page)
        
    except PageNotAnInteger:
        page_object = paginator.page(1)
    
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)

    if cat:
        category = get_object_or_404(Category, name=cat)
        articles = category.article_set.all()
        context['articles'] = articles
        return render(request, 'blog/article_list.html', context)
    
    context['articles'] = page_object
   

    return render(request, 'blog/article_list.html', context)



def article_detail(request, slug):
    article = get_object_or_404(Article, slug_article=slug)

    context = {'article': article}
    return render(request, 'blog/article_detail.html', context)