# Generated by Django 3.1.7 on 2021-04-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_projects', '0009_image_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
