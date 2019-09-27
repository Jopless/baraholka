from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=64, verbose_name='Бренд')

    class Meta:
        verbose_name='Бренд'
        verbose_name_plural='Бренды'

    def __str__(self):
        return self.name


class Sneakers(models.Model):
    model_name = models.CharField(max_length=64, blank=False, verbose_name='Название модели')
    model_brand = models.ForeignKey(Brand, blank=False, on_delete=models.CASCADE, verbose_name='Бренд')
    model_price = models.IntegerField(verbose_name='Цена', blank=True)
    model_time_added = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = 'Кроссовок'
        verbose_name_plural = 'Кроссовки'

    def __str__(self):
        return self.model_name