from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.article_list, name='article-list'),
    path('detail/<slug:slug>', views.article_detail, name='article-detail'),
    path('category/<str:cat>', views.article_list, name='category-list'),
]
