# Generated by Django 3.2.5 on 2021-07-28 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-create_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
