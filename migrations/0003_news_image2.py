# Generated by Django 4.0.4 on 2022-04-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qalampiruz', '0002_news_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
