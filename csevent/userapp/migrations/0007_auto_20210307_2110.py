# Generated by Django 3.1.7 on 2021-03-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_auto_20210307_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='address',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='college_address',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
