from django.db import models


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
        return f'{self.name} {self.datetime_create}'

    class Meta:
        verbose_name = "Название соц сети"
        verbose_name_plural = "Название соц сетей"


class SocialNetwork(models.Model):
    """
    Модель соц сети.
    """
    name = models.ForeignKey(NameSocialNetwork, models.RESTRICT, 'socialnetwork_name',
                             verbose_name='Название соц сети')
    link = models.CharField("Ссылка на соц сеть/месседжер/сайт", max_length=60, null=False)
    datetime_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ссылка на соц сеть"
        verbose_name_plural = "Ссылки на соц сети"
