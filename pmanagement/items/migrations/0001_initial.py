# Generated by Django 3.0.7 on 2020-06-15 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='DateTime on wich the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='DateTime on wich the object was last modiefed', verbose_name='modified at')),
                ('name', models.CharField(max_length=140, verbose_name='item name')),
                ('comments', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='Item/picture')),
                ('supplier', models.CharField(max_length=140)),
                ('cost', models.DecimalField(decimal_places=4, default=0, max_digits=999)),
                ('current_location', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
