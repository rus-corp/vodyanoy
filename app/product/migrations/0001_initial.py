# Generated by Django 4.2 on 2024-05-09 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='слаг')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='category_img/main_category_img', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Главная категория',
                'verbose_name_plural': 'Главные категории',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=220, unique=True, verbose_name='слаг')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='category_img/sub_category_img', verbose_name='Фото')),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='product.maincategory', verbose_name='')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('desc', models.TextField(max_length=800, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('photo', models.ImageField(upload_to='products_img', verbose_name='Фото')),
                ('slug', models.SlugField(max_length=255, verbose_name='слаг')),
                ('retro_bonus', models.PositiveIntegerField(default=1, verbose_name='Ретро бонус за покупку клиенту %')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='manufacturer.manufacturer', verbose_name='производитель')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='product.subcategory', verbose_name='подкатегория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
