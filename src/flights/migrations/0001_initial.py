# Generated by Django 3.2.4 on 2021-06-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=60)),
                ('destination', models.CharField(max_length=60)),
                ('duration', models.TimeField()),
            ],
        ),
    ]
