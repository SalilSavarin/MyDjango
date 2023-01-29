from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    measuring_temperature = models.IntegerField(verbose_name='Температура при измерении')
    date_of_measurement = models.DateTimeField(verbose_name='Дата измерения', auto_now_add=True)
    measurement = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
