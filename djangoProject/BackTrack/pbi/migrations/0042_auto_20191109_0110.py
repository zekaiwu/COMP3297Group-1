# Generated by Django 2.2.5 on 2019-11-08 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbi', '0041_item_started'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='started',
            new_name='added',
        ),
    ]
