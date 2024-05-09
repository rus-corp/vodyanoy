# Generated by Django 4.2 on 2024-05-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название пункта')),
                ('desc', models.TextField(verbose_name='Описание пункта')),
            ],
            options={
                'verbose_name': 'Инфо О нас',
                'verbose_name_plural': 'Инфо О нас',
            },
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('image', models.ImageField(help_text='Максимальное разрешение изображения 2400х600px', upload_to='special_offers/%Y/m', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Спец.предложение на главной странице',
                'verbose_name_plural': 'Спец.предложения на главной странице',
            },
        ),
    ]
