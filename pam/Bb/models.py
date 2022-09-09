from django.db import models


class Owner(models.Model):
    owner = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name_plural = 'Владельцы'
        verbose_name = 'Владелец'
        ordering = ['owner']


class Bb(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    owner = models.ForeignKey('Owner', null=True, on_delete=models.PROTECT, verbose_name='Владелец')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Сотрудник'
        verbose_name = 'Сотрудника'
        ordering = ['-published']
