from django.db import models


class Seller(models.Model):
    seller_name = models.CharField(max_length=100, verbose_name='Поставщик')
    seller = models.CharField(max_length=100, verbose_name='Название')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    adres = models.CharField(max_length=150, verbose_name='Адрес')
    OGRN = models.CharField(max_length=50, verbose_name='ОГРН')
    INN = models.CharField(max_length=50, verbose_name='ИНН')

    def __str__(self):
        return self.seller


class Item(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    avtor = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    articul = models.CharField(max_length=50)
    PG = models.CharField(max_length=10)
    year = models.DateField()
    pages = models.IntegerField()
    type = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    mass = models.IntegerField()
    price = models.IntegerField()
    # pic = models.ImageField()

    def __str__(self):
        return self.name


class Stock(models.Model):
    adres = models.CharField(max_length=50)
    maxcap = models.IntegerField()

    def __str__(self):
        return self.adres


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    bonus = models.CharField(max_length=50)
    datereg = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class ItemsInStock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    count = models.IntegerField()
    # datereg = models.DateField(auto_now_add=True)


class ItemsForBuyer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    count = models.IntegerField()
    # datereg = models.DateField(auto_now_add=True)