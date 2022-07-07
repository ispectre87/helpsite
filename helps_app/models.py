from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Region(models.Model):
    """Список областей """
    region_name = models.CharField(max_length=40, verbose_name= 'Область')

    def __str__(self):
        return self.region_name

    def get_absolute_url(self):
        return reverse('helps_app:cities', kwargs={'region_id': self.id,})

    class Meta():
        verbose_name = 'Список областей'
        verbose_name_plural = 'Список областей'

class City(models.Model):
    """Список городов"""
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Область')
    city_name = models.CharField(max_length=40, verbose_name='Город')

    def __str__(self):
        return self.city_name

    def get_absolute_url(self):
        return reverse('helps_app:help_requests', kwargs={'region_id': self.region_id, 'city_id': self.pk})

    class Meta():
        verbose_name = 'Список городов'
        verbose_name_plural = 'Список городов'
        ordering = ('region', 'city_name')

class HelpRequest(models.Model):
    """Список заявок на помощь"""
    citi_name = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Тип помощи')
    text = models.TextField(verbose_name='Полная информация')
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления') #обновляется при изменении записи
    update = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания') #не обновляется при изменении записи
    contacts = models.TextField(verbose_name='Контакты')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('helps_app:help_request_detail', kwargs={'help_id': self.pk,})

    def edit_record(self):
        return reverse('helps_app:edit_record', kwargs={'help_id': self.pk,})

    class Meta():
        verbose_name = 'Список заявок'
        verbose_name_plural = 'Список заявок'
        ordering = ('update', 'pub_date', )
