from django.db import models


class Assignments (models.Model):
    assigments = models.CharField(max_length=20, db_index=True, verbose_name='Поручения')

    def __str__(self):
        return self.assigments

    class Meta:
        verbose_name_plural = 'Поручения'
        verbose_name = 'Поручения'
        ordering = ['assigments']


class Diovisions (models.Model):
    divisions = models.CharField(max_length=20, db_index=True, verbose_name='Подразделения')

    def __str__(self):
        return self.divisions

    class Meta:
        verbose_name_plural = 'Подразделения'
        verbose_name = 'Подразделения'
        ordering = ['divisions']


class Directions (models.Model):
    directions = models.CharField(max_length=20, db_index=True, verbose_name='Направления деятельности')

    def __str__(self):
        return self.directions

    class Meta:
        verbose_name_plural = 'Направления деятельности'
        verbose_name = 'Направления деятельности'
        ordering = ['directions']


class Customers (models.Model):
    customers = models.CharField(max_length=20, db_index=True, verbose_name='Заказчики')

    def __str__(self):
        return self.customers

    class Meta:
        verbose_name_plural = 'Заказчики'
        verbose_name = 'Заказчики'
        ordering = ['customers']


class Gz (models.Model):
    gz = models.CharField(max_length=20, db_index=True, verbose_name='Госзадание')

    def __str__(self):
        return self.gz

    class Meta:
        verbose_name_plural = 'Госзадание'
        verbose_name = 'Госзадание'
        ordering = ['gz']


class Type_of_objects (models.Model):
    type_of_objects = models.CharField(max_length=20, db_index=True, verbose_name='Виды объектов')

    def __str__(self):
        return self.type_of_objects

    class Meta:
        verbose_name_plural = 'Виды объектов'
        verbose_name = 'Виды объектов'
        ordering = ['type_of_objects']


class Type_of_doing (models.Model):
    type_of_doing = models.CharField(max_length=20, db_index=True, verbose_name='Виды деятельности')

    def __str__(self):
        return self.type_of_doing

    class Meta:
        verbose_name_plural = 'Виды деятельности'
        verbose_name = 'Виды деятельности'
        ordering = ['type_of_doing']


class District(models.Model):
    district = models.CharField(max_length=20, db_index=True, verbose_name='Округа')

    def __str__(self):
        return self.district

    class Meta:
        verbose_name_plural = 'Округа'
        verbose_name = 'Округ'
        ordering = ['district']


class City(models.Model):
    city = models.CharField(max_length=20, db_index=True, verbose_name='Города')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'
        ordering = ['city']


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


class Doc (models.Model):
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    date_end = models.DateField(auto_now_add=False, db_index=True, verbose_name='Дата закрытия')
    state = models.CharField(max_length=50, verbose_name='Статус')
    type_of_doing = models.ForeignKey('Type_of_doing', null=True, on_delete=models.PROTECT, verbose_name='Вид деятельности')
    direction = models.ForeignKey('Directions', null=True, on_delete=models.PROTECT, verbose_name='Направление деятельности')
    type_of_object = models.ForeignKey('Type_of_objects', null=True, on_delete=models.PROTECT, verbose_name='Вид объекта')

    def __str__(self):
        return self.state

    class Meta:
        verbose_name_plural = 'Документ ПАМ'
        verbose_name = 'Документ ПАМ'
        ordering = ['published']
