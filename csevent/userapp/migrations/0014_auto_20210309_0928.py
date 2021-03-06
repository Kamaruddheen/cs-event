# Generated by Django 3.1.7 on 2021-03-09 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_auto_20210309_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='final_test',
            name='placed',
            field=models.CharField(choices=[('selected', 'Selected'), ('notselected', 'Not Selected'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=20),
        ),
        migrations.AlterField(
            model_name='prelim_test',
            name='event',
            field=models.CharField(choices=[('wordhunt', 'Word Hunt'), ('codetreasure', 'Code Treasure'), ('logo', 'Logo Design'), ('poster', 'Poster Design')], max_length=20),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='bonafide',
            field=models.FileField(null=True, upload_to='Student_bonafide'),
        ),
    ]
