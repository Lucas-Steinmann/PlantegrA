# Generated by Django 2.2 on 2019-04-08 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantegra_crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='customer',
        ),
    ]
