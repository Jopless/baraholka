# Generated by Django 2.2.5 on 2019-09-26 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20190926_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakers',
            name='model_time_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
