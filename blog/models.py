from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'catégorie'
        verbose_name_plural = 'catégories'

    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(default=timezone.now)

    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'commentaire'
        verbose_name_plural = 'commentaires'

    def __str__(self):
        return str(self.content)
