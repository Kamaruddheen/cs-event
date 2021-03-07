# Generated by Django 3.1.7 on 2021-03-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20210307_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='final_code_spot_error_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='final_code_spot_error/')),
            ],
        ),
        migrations.RenameField(
            model_name='final_answer_relation',
            old_name='final_code_spot_error_questio',
            new_name='final_code_spot_error_question',
        ),
        migrations.RemoveField(
            model_name='final_code_spot_error_question',
            name='question',
        ),
        migrations.AddField(
            model_name='final_code_spot_error_question',
            name='question',
            field=models.ManyToManyField(to='questions.final_code_spot_error_image'),
        ),
    ]
