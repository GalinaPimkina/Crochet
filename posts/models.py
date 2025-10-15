from django.db import models
from autoslug.fields import AutoSlugField

from users.models import User


class BaseModelClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModelClass):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    image = models.ImageField(upload_to="image/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Изображение")
    body = models.TextField()
    slug = AutoSlugField(populate_from="title", max_length=10, unique=True, db_index=True, verbose_name="Слаг")
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL, related_name="author")

