# Generated by Django 3.1.7 on 2021-03-07 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0002_auto_20210307_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='roundtype',
            field=models.CharField(choices=[('prelims', 'Prelims'), ('final', 'Finals')], default='prelims', max_length=8),
        ),
    ]
