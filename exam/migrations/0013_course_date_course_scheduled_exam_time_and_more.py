# Generated by Django 4.1.3 on 2022-12-09 16:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_course_negative_marking_question_negative_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='scheduled_exam_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='negative_marking',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='negative_marks',
            field=models.FloatField(),
        ),
    ]
