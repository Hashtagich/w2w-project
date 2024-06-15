from django.db import models
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


class Role(models.Model):
    title = models.CharField(
        'Название',
        max_length=64,
    )

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        is_staff = kwargs.pop('is_staff', False)
        is_superuser = kwargs.pop('is_superuser', False)
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password, **kwargs):
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **kwargs,
        )


class User(AbstractBaseUser, PermissionsMixin):
    GENDER = [
        ('man', 'Мужчина'),
        ('woman', 'Женщина'),
    ]

    ZODIAC = [
        ('Aries', 'Овен'),
        ('Taurus', 'Телец'),
        ('Gemini', 'Близнецы'),
        ('Cancer', 'Рак'),
        ('Leo', 'Лев'),
        ('Virgo', 'Дева'),
        ('Libra', 'Весы'),
        ('Scorpio', 'Скорпион'),
        ('Ophiuchus', 'Змееносец'),
        ('Sagittarius', 'Стрелец'),
        ('Capricorn', 'Козерог'),
        ('Aquarius', 'Водолей'),
        ('Pisces', 'Рыбы'),
    ]
    username = models.CharField(
        'Username',
        max_length=128,
        blank=True,
        unique=True,
    )
    first_name = models.CharField(
        'Имя',
        max_length=128,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=128,
        blank=True,
        null=True,
    )
    middle_name = models.CharField(
        'Отчество',
        max_length=128,
        blank=True,
        null=True,
    )
    zodiac = models.CharField(
        "Знак зодиака",
        max_length=20,
        choices=ZODIAC,
        blank=True
    )
    gender = models.CharField(
        "Пол",
        max_length=10,
        choices=GENDER,
        blank=True
    )
    role = models.ForeignKey(
        verbose_name='Роль',
        to=Role,
        on_delete=models.PROTECT,
        related_name='role',
        null=True,
        blank=True,
    )
    phone = models.CharField(
        'Номер телефона',
        max_length=15,
        blank=True,
        null=True,
        unique=True,
    )
    email = models.EmailField(
        'Email',
        null=False,
        unique=True,
    )
    photo = models.FileField(
        'Фотография',
        upload_to='users/',
        blank=True,
        null=True
    )
    telegram = models.CharField(
        'Ник в телеграме',
        max_length=128,
        blank=True,
        null=True,
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'