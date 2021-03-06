# Generated by Django 2.2.6 on 2019-10-25 05:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pbi', '0013_auto_20191025_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('Guest', 'Guest'), ('Developer', 'Developer'), ('ScrumMaster', 'ScrumMaster'), ('ProductOwner', 'ProductOwner')], default='GUEST', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='create_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
