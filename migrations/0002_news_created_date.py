# Generated by Django 4.0.4 on 2022-04-22 14:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qalampiruz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
