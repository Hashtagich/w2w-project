from django.db import models
from .other import NumberSubscribers, AverageCheck, Interest
from collaborations.models.collaboration import Collaboration
from accounts.models import User


# Create your models here.

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
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    number_subscribers = models.ForeignKey(NumberSubscribers, on_delete=models.PROTECT,
                                           verbose_name="Кол-во подписчиков", blank=True)
    average_check = models.ForeignKey(AverageCheck, on_delete=models.PROTECT, verbose_name='Средний чек', blank=True,
                                      null=True)
    avatar_id = models.ImageField("Аватар", upload_to=get_image_path_brand, blank=True, null=True)
    value = models.CharField("Ценности бренда", max_length=256, null=True, blank=True)
    target_audience = models.TextField("Целевая аудитория", null=True, blank=True)
    link = models.URLField("Ссылка на сайт бренда", max_length=200, null=False)
    description = models.TextField("О бренде/описание", null=True, blank=True)
    geo = models.CharField("ГЕО", max_length=256, null=True, blank=True)
    balance = models.IntegerField("Баланс", null=True, default=1)
    experience = models.IntegerField("Опыт", null=True, default=1)
    level = models.IntegerField("Уровень", null=True, default=1)
    modifier = models.IntegerField("Модификатор", null=True, default=1)

    datetime_create = models.DateTimeField(auto_now_add=True)

    interests = models.ManyToManyField(
        Interest,
        related_name='brand_interest',
        blank=True,
        verbose_name='Интересы',
        through='BrandInterest'
    )

    category = models.ManyToManyField(
        'Category',
        related_name='brand_category',
        blank=True,
        verbose_name='Категории',
        through='BrandCategory'
    )

    collaboration = models.ManyToManyField(
        Collaboration,
        related_name='brand_collaboration',
        blank=True,
        verbose_name='Коллаборации',
        through='BrandCollaboration'
    )

    def __str__(self):
        return f'{self.name} - {self.status}'

    def modifier_up(self, point: int = 1):
        """
        Метод увеличения модификатора баланса бренда пользователя. Увеличивается на величину point, по дефолту = 1.
        """
        self.modifier += point

    def level_up(self, point: int = 1):
        """Метод увеличения уровня бренда пользователя. Увеличивается на величину point, по дефолту = 1."""
        self.level += point

    def balance_up(self, point: int = 1):
        """
        Метод увеличения баланса(внутренняя валюта) бренда пользователя.
        Увеличивается на величину point с учётом модификатора, по дефолту = 1.
        Модификатор зависит от тарифа.
        """
        self.balance += (point * self.modifier)

    def experience_up(self, point: int = 1):
        """
        Метод увеличения рейтинга/опыта бренда пользователя. Увеличивается на величину point, по дефолту = 1.
        Как только становиться больше или равен 100 то уменьшается на 100 и автоматически повышает уровень пользователя
        на 1 и баланс на 10 с учётом модификатора.
        """
        self.experience += point
        if self.experience >= 100:
            self.experience -= 100
            self.balance_up(point=10)
            self.level_up()

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


class BrandInterest(models.Model):
    """Модель связи бренда и интереса."""
    brand_id = models.ForeignKey(
        Brand, models.PROTECT, related_name='brands_interests', verbose_name='ID бренда'
    )
    interest_id = models.ForeignKey(
        Interest, models.PROTECT, related_name='interests', verbose_name='ID интереса'
    )

    def __str__(self):
        return f'({self.pk}) {self.brand_id}'

    class Meta:
        verbose_name = 'Сводная таблица бренда и интерес'
        verbose_name_plural = 'Сводные таблицы бренды и интересы'
        ordering = ('-brand_id', 'interest_id',)
