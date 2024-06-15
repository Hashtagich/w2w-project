from django.db import models
from brands.models.other import NumberSubscribers, AverageCheck


# from accounts.models import User


def get_image_path_collaboration(instance, filename):
    """
    Функция для прописывания пути сохранения изображений. Если не будет найдено последнего (ни одного) объекта,
    то будет создана папка с id (окончанием) 0.
    """
    last_object = Collaboration.objects.last()

    if last_object is not None:
        return f'static/photos/collaboration-{last_object.id}/{filename}'
    else:
        return f'static/photos/collaboration-0/{filename}'


class Collaboration(models.Model):
    """Модель коллаборации."""
    # CHOICE_STATUS = (
    #     ("", ""),
    #     ("", ""),
    #     ("", ""),
    #     ("", ""),
    #
    # )

    name = models.CharField("Название коллаборации", max_length=30, null=True)
    # status = models.CharField("Статус", max_length=50, choices=CHOICE_STATUS, default="")
    avatar_id = models.ImageField("Аватар", upload_to=get_image_path_collaboration, blank=True, null=True)
    description = models.TextField("Описание коллаборации", null=True, blank=True)
    number_subscribers = models.ForeignKey(NumberSubscribers, on_delete=models.PROTECT,
                                           verbose_name="Кол-во подписчиков", blank=True)
    average_check = models.ForeignKey(AverageCheck, on_delete=models.PROTECT, verbose_name='Средний чек', blank=True)
    result = models.TextField("Результат коллаборации", null=True, blank=True)

    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Коллаборация"
        verbose_name_plural = "Коллаборации"
        ordering = ('name',)


class FotoCollaboration(models.Model):
    """Модель фотографии коллаборации."""
    foto = models.ImageField("Фотография", upload_to=get_image_path_collaboration, blank=True, null=True)
    description = models.CharField("Описание фотографии", max_length=255, null=True, blank=True)
    collaboration_id = models.ForeignKey(
        Collaboration, models.PROTECT, 'collaboration_foto', verbose_name='ID коллаборации'
    )

    def __str__(self):
        return f'{self.description} ({self.pk})'

    class Meta:
        verbose_name = 'Фотография коллаборации'
        verbose_name_plural = 'Фотографии коллаборации'


class Task(models.Model):
    """Модель задачи."""
    CHOICE_STATUS = (
        ("new", 'Создана'),
        ("in_progress", "В процессе"),
        ("done", "Завершена"),
    )
    name = models.CharField("Название задачи/этапа", max_length=60, null=True, default="Этап/задача №1")
    status = models.CharField("Статус", max_length=50, choices=CHOICE_STATUS, default="new")
    description = models.TextField("Описание задачи/этапа", null=True, blank=True)

    collaboration_id = models.ForeignKey(
        Collaboration, models.PROTECT, 'collaboration_task', verbose_name='Коллаборация'
    )
    # author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь/автор", blank=True)

    datetime_start = models.DateTimeField("Дата начала задачи/этапа", blank=True)
    datetime_completion = models.DateTimeField("Дата когда задача/этап должна быть выполнена", blank=True)
    datetime_finish = models.DateTimeField("Дата окончания задачи/этапа", blank=True)
    datetime_create = models.DateTimeField("Дата создания задачи/этапа", auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} - {self.status}'

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ('status', 'name')
