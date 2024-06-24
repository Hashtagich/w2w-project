from django.db import models
from brands.models import Brand
# Create your models here.


class Chat(models.Model):
    brands = models.ManyToManyField(Brand, related_name='chat')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        names = ', '.join([brand.name for brand in self.brands.all()])
        return f'Чат между: {names}'

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = "Чаты"


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='message', on_delete=models.CASCADE)
    body = models.TextField()
    receiver = models.ForeignKey(Brand, related_name='received_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(Brand, related_name='sent_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Сообщение от {self.author} к {self.receiver}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = "Сообщения"