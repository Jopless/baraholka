# Generated by Django 2.2.5 on 2019-09-26 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20190926_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakers',
            name='model_date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]