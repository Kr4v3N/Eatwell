from django.db import models


# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = 'À propos'
        verbose_name_plural = 'À propos'

    def __str__(self):
        return self.title


class Why_Choose_us(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'Pourquoi nous'
        verbose_name_plural = 'Pourquoi nous'

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='chef/')

    class Meta:
        verbose_name = 'Notre Chef'
        verbose_name_plural = 'Nos Chefs'

    def __str__(self):
        return self.name
