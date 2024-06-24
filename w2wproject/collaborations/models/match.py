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
            # if created:
            # в будущем прописать логику для создания чата из приложения chat
            #     Chat.objects.create(match=match)
            # else:
            #     Chat.objects.get_or_create(match=match)


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
