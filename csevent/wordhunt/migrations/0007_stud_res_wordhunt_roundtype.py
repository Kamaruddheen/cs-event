# Generated by Django 3.1.7 on 2021-03-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordhunt', '0006_score_wordhuntmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud_res_wordhunt',
            name='roundtype',
            field=models.CharField(choices=[('prelims', 'Prelims'), ('final', 'Finals')], default='prelims', max_length=8),
        ),
    ]
