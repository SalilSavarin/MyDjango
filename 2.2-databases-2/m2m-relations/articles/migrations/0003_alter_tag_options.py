# Generated by Django 4.1.2 on 2023-01-19 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
