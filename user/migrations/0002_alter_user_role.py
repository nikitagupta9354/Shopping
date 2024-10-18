# Generated by Django 5.1.2 on 2024-10-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Owner'), (2, 'Customer')], default=2, null=True),
        ),
    ]
