# Generated by Django 2.0.7 on 2018-08-16 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20180816_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
