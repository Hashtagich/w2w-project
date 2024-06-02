from django.db import models
from .other import NumberSubscribers, AverageCheck
from .customer import Customer
from .collaboration import Collaboration


def get_image_path_brand(instance, filename):
    """
    Функция для прописывания пути сохранения изображений. Если не будет найдено последнего (ни одного) объекта,
    то будет создана папка с id (окончанием) 0.
    """
    last_object = Brand.objects.last()

    if last_object is not None:
        return f'static/photos/brand-{last_object.id}/{filename}'
    else:
        return f'static/photos/brand-0/{filename}'


class Brand(models.Model):
    """Модель бренда."""
    CHOICE_STATUS = (
        ("new", 'новый'),
        ("pending", 'модератор взял в работу'),
        ("accepted", 'модерация прошла успешно'),
        ("rejected", 'модерация прошла, информация не принята'),
    )

    name = models.CharField("Название бренда", max_length=30, null=True)
    status = models.CharField("Статус", max_length=50, choices=CHOICE_STATUS, default="new")
    author = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name="Пользователь/автор")
    number_subscribers = models.ForeignKey(NumberSubscribers, on_delete=models.PROTECT,
                                           verbose_name="Кол-во подписчиков")
    average_check = models.ForeignKey(AverageCheck, on_delete=models.PROTECT, verbose_name='Средний чек')
    avatar_id = models.ImageField("Аватар", upload_to=get_image_path_brand, blank=True, null=True)
    value = models.CharField("Ценности бренда", max_length=256, null=True, blank=True)
    target_audience = models.TextField("Описание ЦА", null=True, blank=True)
    geo = models.CharField("ГЕО", max_length=256, null=True, blank=True)

    datetime_create = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    category = models.ManyToManyField(
        'Category',
        related_name='brand_category',
        blank=True,
        verbose_name='Категории',
        through='BrandCategory'
    )

    collaboration = models.ManyToManyField(
        'Collaboration',
        related_name='brand_collaborations',
        blank=True,
        verbose_name='Коллаборации',
        through='BrandCollaboration'
    )

    def __str__(self):
        return f'{self.name} - {self.status}'

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
        ordering = ('status', 'name')


class Category(models.Model):
    """Модель категорий брендов."""
    name = models.CharField("Название категории", max_length=60, null=False, unique=True)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField("Активность", default=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('name',)


class FotoBrand(models.Model):
    """Модель фотографии бренда."""
    foto = models.ImageField("Фотография", upload_to=get_image_path_brand, blank=True, null=True)
    description = models.CharField("Описание фотографии", max_length=255, null=True, blank=True)
    brand_id = models.ForeignKey(
        Brand, models.PROTECT, 'brand_foto', verbose_name='ID бренда'
    )

    def __str__(self):
        return f'{self.description} ({self.pk})'

    class Meta:
        verbose_name = 'Фотография бренда'
        verbose_name_plural = 'Фотографии бренда'


class BrandCategory(models.Model):
    """Модель связи бренд и категория."""
    brand_id = models.ForeignKey(
        Brand, models.PROTECT, 'brands_categories', verbose_name='ID бренда'
    )
    category_id = models.ForeignKey(
        Category, models.PROTECT, 'categories', verbose_name='Категория'
    )

    def __str__(self):
        return f'({self.pk}) {self.brand_id}'

    class Meta:
        verbose_name = 'Сводная таблица бренд и категория'
        verbose_name_plural = 'Сводная таблица бренды и категории'
        ordering = ('-brand_id', 'category_id',)


class BrandCollaboration(models.Model):
    """Модель связи бренд и коллаборации."""
    brand_id = models.ForeignKey(
        Brand, models.PROTECT, 'brands_collaborations', verbose_name='ID бренда'
    )
    collaboration_id = models.ForeignKey(
        Collaboration, models.PROTECT, 'collaborations', verbose_name='Коллаборация'
    )

    def __str__(self):
        return f'({self.pk}) {self.brand_id}'

    class Meta:
        verbose_name = 'Сводная таблица бренд и коллаборации'
        verbose_name_plural = 'Сводная таблица бренды и коллаборации'
        ordering = ('-brand_id', 'collaboration_id',)
