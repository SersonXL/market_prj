# Generated by Django 3.2.25 on 2024-06-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20240527_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='availability',
            field=models.PositiveIntegerField(verbose_name='Количество свободных номеров'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание продукта'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Название проживания'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='room_desc',
            field=models.TextField(blank=True, max_length=60, verbose_name='Краткое описание комнаты'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='short_desc',
            field=models.TextField(blank=True, max_length=60, verbose_name='Краткое описание продукта'),
        ),
        migrations.AlterField(
            model_name='listofcountries',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='listofcountries',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AlterField(
            model_name='listofcountries',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Имя'),
        ),
    ]
