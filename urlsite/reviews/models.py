from django.db import models

class Review(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Текст отзыва')
    is_checked = models.BooleanField(default=False, verbose_name='Проверено')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'