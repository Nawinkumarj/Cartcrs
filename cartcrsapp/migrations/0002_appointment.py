# Generated by Django 5.0 on 2024-03-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartcrsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('department', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
