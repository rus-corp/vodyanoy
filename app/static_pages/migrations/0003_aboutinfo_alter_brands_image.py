# Generated by Django 4.2 on 2024-05-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0002_brands'),
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
        migrations.AlterField(
            model_name='brands',
            name='image',
            field=models.ImageField(blank=True, help_text='Перед загрузкой удалить фон у фото', null=True, upload_to='', verbose_name='Лого бренда'),
        ),
    ]
