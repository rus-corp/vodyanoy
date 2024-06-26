# Generated by Django 4.2 on 2024-05-09 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManufacturerCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('image', models.FileField(upload_to='country_flags/', verbose_name='Флаг')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Страна производителя',
                'verbose_name_plural': 'Страны производителей',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='слаг')),
                ('image', models.FileField(upload_to='manufacturer_img/', verbose_name='Логотип')),
                ('price_segment', models.CharField(choices=[('econom', 'эконом'), ('middle', 'средний'), ('premium', 'премиум')], default=('middle', 'средний'), max_length=20, verbose_name='Ценовой сегмент')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='manufacurers', to='manufacturer.manufacturercountry', verbose_name='страна')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
    ]
