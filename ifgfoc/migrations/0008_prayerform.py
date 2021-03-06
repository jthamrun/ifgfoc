# Generated by Django 3.0.8 on 2020-08-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifgfoc', '0007_auto_20200813_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='prayerForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('phoneNumber', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=40)),
                ('prayerRequest', models.TextField()),
            ],
            options={
                'verbose_name': 'Prayer Card',
            },
        ),
    ]
