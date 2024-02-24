from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    """ Модель контактов """

    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=10, verbose_name='Номер дома', **NULLABLE)

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Product(models.Model):
    """ Модель продуктов """

    title = models.CharField(max_length=100, verbose_name='Наименование продукта')
    model = models.CharField(max_length=100, verbose_name='Модель продукта', **NULLABLE)
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок', **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Supplier(models.Model):
    """ Модель поставщиков """

    FACTORY = '0'
    RETAIL_NETWORK = '1'
    INDIVIDUAL_ENTREPRENEUR = '2'

    LEVEL_TYPE = (
        (FACTORY, 'Завод'),
        (RETAIL_NETWORK, 'Розничная сеть'),
        (INDIVIDUAL_ENTREPRENEUR, 'Индивидуальный предприниматель')
    )

    name = models.CharField(max_length=100, verbose_name='Название поставщика')
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, verbose_name='Контакт', **NULLABLE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Продукт', **NULLABLE)
    level = models.IntegerField(choices=LEVEL_TYPE, verbose_name='Уровень поставщика')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'


class Seller(models.Model):
    """ Модель продавца """

    name = models.CharField(max_length=100, verbose_name='Название продавца')
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, verbose_name='Контакт', **NULLABLE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Продукт', **NULLABLE)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Задолженность поставщику')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Время создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продавец'
        verbose_name_plural = 'продавцы'
