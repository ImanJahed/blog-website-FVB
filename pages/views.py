from django.shortcuts import render

from blog.models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()
    
    context = {'articles': articles}
    return render(request, 'pages/home.html', context)