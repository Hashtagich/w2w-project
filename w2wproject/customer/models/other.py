from django.db import models


class AverageCheck(models.Model):
    """
    Модель среднего чека бренда. Можно создавать сколько угодно объектов для дальнейшего выбора из списка
    в других моделях или формах. Активность означает отображение данного объекта в списке т.е.
    можно заранее сделать большой список, а отображать только часть.
    """
    name = models.CharField("Средний чек бренда", max_length=60, null=False)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField("Активность", default=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} от {self.datetime_create.strftime("%d %B %Y %H:%M:%S")}'

    class Meta:
        verbose_name = "Средний чек бренда"
        verbose_name_plural = "Средние чеки бренда"


class NumberSubscribers(models.Model):
    """
    Модель количества подписчиков. Можно создавать сколько угодно объектов для дальнейшего выбора из списка
    в других моделях или формах. Активность означает отображение данного объекта в списке т.е.
    можно заранее сделать большой список, а отображать только часть.
    """
    name = models.CharField("Кол-во подписчиков", max_length=60, null=False)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField("Активность", default=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} от {self.datetime_create.strftime("%d %B %Y %H:%M:%S")}'

    class Meta:
        verbose_name = "Кол-во подписчиков"
        verbose_name_plural = "Кол-во подписчиков"


class Interest(models.Model):
    """
    Модель интересов/тегов. Можно создавать сколько угодно объектов для дальнейшего выбора из списка
    в других моделях или формах. Активность означает отображение данного объекта в списке т.е.
    можно заранее сделать большой список, а отображать только часть.
    """
    name = models.CharField("Интерес/тег", max_length=60, null=False)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField("Активность", default=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} от {self.datetime_create.strftime("%d %B %Y %H:%M:%S")}'

    class Meta:
        verbose_name = "Интерес/тег"
        verbose_name_plural = "Интересы/теги"


class FAQ(models.Model):
    """Модель ответов на часто задаваемые вопросы."""
    question = models.TextField(null=True, verbose_name="Вопрос")
    answer = models.TextField(null=True, verbose_name="Ответ")

    def __str__(self):
        return f'{self.question}'

    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "Часто задаваемые вопросы"


class MagicBall(models.Model):
    prediction = models.CharField(null=False, blank=False)

    def __str__(self):
        return f'{self.prediction}'

    class Meta:
        verbose_prediction = "Предсказание"
        verbose_name_plural = "Предсказания"