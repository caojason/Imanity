# Generated by Django 2.0.7 on 2018-08-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180815_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='s', max_length=200),
            preserve_default=False,
        ),
    ]
