# Generated by Django 4.2 on 2024-05-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название новости')),
                ('desc', models.TextField(verbose_name='Текст новости')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/%Y/%m/%d', verbose_name='Фото обложки новости')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отоброжение на сайте')),
                ('slug', models.SlugField(max_length=255, verbose_name='слаг')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
