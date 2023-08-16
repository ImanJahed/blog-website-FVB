from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article, Category, Comment

# Create your views here.
def article_list(request, cat=None):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    context = {}

    try:
        page_object = paginator.get_page(page)
        
    except PageNotAnInteger:
        page_object = paginator.page(1)
    
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)

    if cat:
        category = get_object_or_404(Category, name=cat)
        articles = category.article_set.all()
        paginator = Paginator(articles, 2)
        page_object = paginator.get_page(page)

        context['articles'] = page_object
        return render(request, 'blog/article_list.html', context)
    
    context['articles'] = page_object
 

    return render(request, 'blog/article_list.html', context)



def article_detail(request, slug):
    article = get_object_or_404(Article, slug_article=slug)
    if request.method == 'POST':
        comment = request.POST.get('text')
        parent_id = request.POST.get('parent')
        
        Comment.objects.create(article=article, user=request.user, text=comment, parent_id=parent_id)
    context = {'article': article}
    return render(request, 'blog/article_detail.html', context)




def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')

    page_object = paginator.get_page(page)

    context = {'articles': page_object}
    return render(request, 'blog/article_list.html',context )


def liked(request, pk):
    article= Article.objects.get(pk=pk)

    if request.user in article.like.all():
        article.like.remove(request.user)
        return JsonResponse({'status':'unliked'})

    else:
        article.like.add(request.user)
        return JsonResponse({'status':'liked'})

    
        

