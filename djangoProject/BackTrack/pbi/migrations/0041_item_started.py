# Generated by Django 2.2.5 on 2019-11-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbi', '0040_scrummaster_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='started',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
