# Generated by Django 3.1.1 on 2020-10-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_auto_20201020_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_pinned',
            field=models.BooleanField(default=False, verbose_name='Is Pinned'),
        ),
    ]