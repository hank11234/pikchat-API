# Generated by Django 3.0 on 2021-02-22 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='picture_id',
            new_name='picture',
        ),
    ]
