# Generated by Django 3.1.6 on 2021-02-15 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_projects', '0005_auto_20210215_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='folder',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
