# Generated by Django 3.1.7 on 2021-03-07 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_auto_20210307_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='user',
            field=models.OneToOneField(limit_choices_to=models.Q(user_type=3), on_delete=django.db.models.deletion.PROTECT, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
