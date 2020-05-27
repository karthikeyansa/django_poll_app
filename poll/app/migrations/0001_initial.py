# Generated by Django 3.0.5 on 2020-05-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice1_count', models.IntegerField(default=0)),
                ('choice2_count', models.IntegerField(default=0)),
            ],
        ),
    ]
