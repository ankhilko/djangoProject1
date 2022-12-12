from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
        unique=True,
        verbose_name='название',
        help_text='Не более 64 символов',
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='опубликовано',
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        db_table = 'blog_categories'


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='заголовок',
    )
    descr = models.TextField(
        verbose_name='описание'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='дата публикации',
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='дата создания',
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name='категория',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
    )

    def __str__(self):
        return self.title

    # можем использовать вместо date_created
    @property
    def date(self) -> str:
        return self.date_created.strftime("%Y-%m-%d")

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        db_table = 'blog_posts'
        ordering = ['date_created']    # можно описать и в админке и в мете





