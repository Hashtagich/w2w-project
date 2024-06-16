from django.db import models


# Create your models here.

def get_image_path_brand(instance, filename):
    """
    Функция для прописывания пути сохранения изображений. Если не будет найдено последнего (ни одного) объекта,
    то будет создана папка с id (окончанием) 0.
    """
    last_object = Post.objects.last()

    if last_object is not None:
        return f'static/photos/post-{last_object.id}/{filename}'
    else:
        return f'static/photos/post-0/{filename}'


class Post(models.Model):
    """Модель новости для раздела комьюнити. """
    title = models.CharField("Заголовок", max_length=200, null=True, blank=True)
    text = models.TextField("Текст", null=True, blank=True)
    avatar_id = models.ImageField("Аватар", upload_to=get_image_path_brand, blank=True, null=True)
    link = models.URLField("Ссылка на пост", max_length=200, null=False, blank=True)
    is_active = models.BooleanField("Активность", default=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} от {self.datetime_create.strftime("%d %B %Y %H:%M:%S")}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
