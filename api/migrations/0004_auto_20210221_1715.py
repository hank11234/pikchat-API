# Generated by Django 3.0 on 2021-02-21 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210221_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to=settings.AUTH_USER_MODEL),
        ),
    ]
