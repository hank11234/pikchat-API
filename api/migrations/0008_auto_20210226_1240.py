# Generated by Django 3.0 on 2021-02-26 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210222_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='picture_id',
            new_name='pictureId',
        ),
    ]
