# Generated by Django 2.2 on 2019-10-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantegra_resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image'),
        ),
    ]
