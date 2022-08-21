
from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Текст статьи')
    published_at = models.DateTimeField(verbose_name='Опубликовано')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']


    def __str__(self):
        return self.title


class Tag(models.Model):

    name = models.CharField(max_length=40, verbose_name='Название')
    articles = models.ManyToManyField(Article, through='ArticleScope')

    class Meta:
        verbose_name = 'Тематический раздел'
        verbose_name_plural = 'Тематические разделы'

    def __str__(self):
        return self.name


class ArticleScope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name='Основной', default=False)

    class Meta:
        verbose_name = 'Тематический раздел'
        verbose_name_plural = 'Тематические разделы'
        ordering = ['-is_main']