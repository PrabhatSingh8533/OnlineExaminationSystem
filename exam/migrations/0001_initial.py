# Generated by Django 4.1.2 on 2022-11-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.IntegerField()),
                ('ques', models.CharField(max_length=140)),
                ('OptA', models.CharField(max_length=40)),
            ],
        ),
    ]
