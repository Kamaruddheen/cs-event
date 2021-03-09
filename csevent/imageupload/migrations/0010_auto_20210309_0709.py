# Generated by Django 3.1.7 on 2021-03-09 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0009_auto_20210309_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]