from django.db import models

class Region(models.Model):
    region_name = models.CharField(max_length=40, verbose_name= 'Область')

    def __str__(self):
        return self.region_name

    class Meta():
        verbose_name = 'Список областей'
        verbose_name_plural = 'Список областей'

class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Область')
    city_name = models.CharField(max_length=40, verbose_name='Город')

    def __str__(self):
        return self.city_name

    class Meta():
        verbose_name = 'Список городов'
        verbose_name_plural = 'Список городов'
        ordering = ('region', 'city_name')


class HelpRequest(models.Model):
    citi_name = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    title = models.CharField(max_length=200, verbose_name='Тип помощи')
    text = models.TextField(verbose_name='Полная информация')
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата обновления')
    contacts = models.TextField(verbose_name='Контакты')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Список заявок'
        verbose_name_plural = 'Список заявок'
        ordering = ('update', 'pub_date', )
