# Generated by Django 2.1.8 on 2019-06-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190606_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsforbuyer',
            name='datereg',
        ),
        migrations.RemoveField(
            model_name='itemsinstock',
            name='datereg',
        ),
        migrations.AlterField(
            model_name='seller',
            name='INN',
            field=models.CharField(max_length=50, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='OGRN',
            field=models.CharField(max_length=50, verbose_name='ОГРН'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='adres',
            field=models.CharField(max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_name',
            field=models.CharField(max_length=100, verbose_name='Поставщик'),
        ),
    ]
