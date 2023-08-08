from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from blog.models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()

    context = {'articles': articles,  }
    return render(request, 'pages/home.html', context)


def sidbar(request):
    recent_articles = Article.objects.order_by('-created_date')[:3]
    context = {'recent': recent_articles}
    return render(request, 'partial/side_bar.html', context)