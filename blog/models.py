from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.

class ArticlesManage(models.Manager):
    def get_queryset(self):
        
        return super().get_queryset().filter(is_published=True)

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='img', null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('Category')
    slug_article = models.SlugField(blank=True)

    objects = models.Manager()
    article = ArticlesManage()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug_article})

    def save(self, *args, **kwargs):
        self.slug_article = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    text = models.TextField()

    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True , related_name='replies')

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text