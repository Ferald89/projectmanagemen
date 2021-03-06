# Generated by Django 3.0.7 on 2020-06-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0002_auto_20200615_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projectmembers', through='projects.Membership', to='users.User'),
        ),
    ]
