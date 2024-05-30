from django.db import models


class Customer(models.Model):
    """Модель пользователя."""
    GENDER = [
        ('man', 'Мужчина'),
        ('woman', 'Женщина'),
    ]

    name = models.CharField("Имя пользователя", max_length=30, null=True)
    surname = models.CharField("Фамилия пользователя", max_length=30, null=True)
    patronymic = models.CharField("Отчество пользователя", max_length=30, null=True, blank=True)
    nickname = models.CharField("Никнейм пользователя", max_length=30, null=True, blank=True)
    email = models.EmailField("Эл.почта пользователя", max_length=100, null=True)
    phone = models.CharField("Контактный телефон", max_length=12, null=True)
    balance = models.IntegerField("Баланс", null=True, default=1)
    experience = models.IntegerField("Опыт", null=True, default=1)
    level = models.IntegerField("Уровень", null=True, default=1)
    modifier = models.IntegerField("Модификатор", null=True, default=1)
    gender = models.CharField("Пол", max_length=10, choices=GENDER)
    status = models.ForeignKey("Role", on_delete=models.PROTECT, verbose_name="Роль")
    tariff = models.ForeignKey("Tariff", on_delete=models.PROTECT, related_name='tariff')
    datetime_create = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    # interests = models.ManyToManyField('Interests',
    #                                    related_name='customer_Interests',
    #                                    blank=True,
    #                                    verbose_name='Интересы',
    #                                    through='CustomerInterests'
    #                                    )

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} уровень {self.level}'

    def modifier_up(self, point: int = 1):
        """Метод увеличения модификатора баланса пользователя. Увеличивается на величину point, по дефолту = 1."""
        self.modifier += point

    def level_up(self, point: int = 1):
        """Метод увеличения уровня пользователя. Увеличивается на величину point, по дефолту = 1."""
        self.level += point

    def balance_up(self, point: int = 1):
        """
        Метод увеличения баланса(внутренняя валюта) пользователя.
        Увеличивается на величину point с учётом модификатора, по дефолту = 1.
        Модификатор зависит от тарифа.
        """
        self.balance += (point * self.modifier)

    def experience_up(self, point: int = 1):
        """
        Метод увеличения рейтинга/опыта пользователя. Увеличивается на величину point, по дефолту = 1.
        Как только становиться больше или равен 100 то уменьшается на 100 и автоматически повышает уровень пользователя
        на 1 и баланс на 10 с учётом модификатора.
        """
        self.experience += point
        if self.experience >= 100:
            self.experience -= 100
            self.balance_up(point=10)
            self.level_up()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('surname', 'name', 'balance')


class Tariff(models.Model):
    """Модель тарифа пользователя."""
    name = models.CharField("Название тарифа", max_length=30, null=True)
    price = models.IntegerField("Стоимость тарифа", null=True)
    description = models.TextField("Описание тарифа", null=True, blank=True)
    duration = models.IntegerField("Длительность тарифа", null=True, default=12)
    datetime_create = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} {self.price} в год'

    def duration_down(self, point: int = 1):
        """Метод уменьшения длительности тарифа на величину point, по дефолту = 1."""
        self.duration -= point

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"


class Role(models.Model):
    """
    Модель модели пользователя. Можно создавать сколько угодно объектов для дальнейшего выбора из списка
    в других моделях или формах. Активность означает отображение данного объекта в списке т.е.
    можно заранее сделать большой список, а отображать только часть.
    """
    name = models.CharField("Название роли", max_length=20, null=False)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField("Активность", default=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Роль пользователя"
        verbose_name_plural = "Роли пользователей"
