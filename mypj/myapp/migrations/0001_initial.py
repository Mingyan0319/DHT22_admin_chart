# Generated by Django 3.1.7 on 2021-02-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DHT22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.DecimalField(decimal_places=2, max_digits=4)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=4)),
                ('time', models.DateTimeField(blank=True)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
