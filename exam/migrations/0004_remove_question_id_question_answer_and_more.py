# Generated by Django 4.1.2 on 2022-11-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default='write your answer here', max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='qno',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
