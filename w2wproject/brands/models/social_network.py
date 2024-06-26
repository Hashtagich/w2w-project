from django.db import models
from .brand import Brand


class NameSocialNetwork(models.Model):
    """
    Модель названия соцсетей/контактных сайтов/месседжеров. Можно создавать сколько угодно объектов для дальнейшего
    выбора из списка в других моделях или формах. Активность означает отображение данного объекта в списке т.е.
    можно заранее сделать большой список, а отображать только часть.
    """
    name = models.CharField("Название соц сети/месседжера/сайта", max_length=60, null=False)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField("Активность", default=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} от {self.datetime_create.strftime("%d %B %Y %H:%M:%S")}'

    class Meta:
        verbose_name = "Название соц сети"
        verbose_name_plural = "Название соц сетей"


class SocialNetwork(models.Model):
    """
    Модель соц сети.
    """
    name = models.ForeignKey(NameSocialNetwork, models.RESTRICT, 'socialnetwork_name',
                             verbose_name='Название соц сети')
    link = models.URLField("Ссылка на соц сеть/месседжер", max_length=200, null=False)
    datetime_create = models.DateTimeField(auto_now_add=True)
    brand_id = models.ForeignKey(
        Brand, models.PROTECT, 'brand_social_network', verbose_name='ID бренда'
    )

    def __str__(self):
        return f'{self.name.name}: {self.link}'

    class Meta:
        verbose_name = "Ссылка на соц сеть"
        verbose_name_plural = "Ссылки на соц сети"
