# Generated by Django 3.1.7 on 2021-03-07 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordhunt', '0003_auto_20210305_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='Wordhunt/'),
        ),
    ]