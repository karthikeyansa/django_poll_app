# Generated by Django 3.0.8 on 2021-03-17 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_posts_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
