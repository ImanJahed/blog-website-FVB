from blog.models import Article, Category


def recent_articles(request):
    recent_articles = Article.objects.order_by('-created_date')[:3]
    return {'recent': recent_articles}

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}