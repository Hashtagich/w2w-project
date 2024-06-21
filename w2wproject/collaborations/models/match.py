from django.db import models

class Like(models.Model):
    from_brand = models.ForeignKey('brands.Brand', related_name='given_likes', on_delete=models.CASCADE)
    to_brand = models.ForeignKey('brands.Brand', related_name='received_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_brand', 'to_brand')
        verbose_name_plural = 'Лайки'
        verbose_name = 'Лайк'

    def __str__(self):
        return f"{self.from_brand} likes {self.to_brand}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.check_for_match_and_chat()

    def check_for_match_and_chat(self):
        reverse_like_exists = Like.objects.filter(from_brand=self.to_brand, to_brand=self.from_brand).exists()
        if reverse_like_exists:
            match, created = Match.objects.get_or_create(
                brand1=min(self.from_brand, self.to_brand, key=lambda b: b.id),
                brand2=max(self.from_brand, self.to_brand, key=lambda b: b.id)
            )
            if created:
                Chat.objects.create(match=match)
            else:
                Chat.objects.get_or_create(match=match)

class Match(models.Model):
    brand1 = models.ForeignKey('brands.Brand', related_name='matches_as_brand1', on_delete=models.CASCADE)
    brand2 = models.ForeignKey('brands.Brand', related_name='matches_as_brand2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('brand1', 'brand2')
        verbose_name_plural = 'Мэтчи'
        verbose_name = 'Мэтч'

    def __str__(self):
        return f"Мэтч: {self.brand1} и {self.brand2}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Chat(models.Model):
    match = models.OneToOneField(Match, related_name='chat', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Чаты'
        verbose_name = 'Чат'

    def __str__(self):
        return f"Чат между {self.match.brand1} и {self.match.brand2}"

    @property
    def participants(self):
        return [self.match.brand1, self.match.brand2]

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey('brands.Brand', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'

    def __str__(self):
        return f"Сообщение от {self.sender} в чате {self.chat}"