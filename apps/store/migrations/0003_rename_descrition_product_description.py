# Generated by Django 3.2.12 on 2022-05-12 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220512_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descrition',
            new_name='description',
        ),
    ]
