# Generated by Django 4.1.7 on 2023-05-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('Sname', models.CharField(max_length=100)),
                ('Sid', models.IntegerField(primary_key=True, serialize=False)),
                ('Saddress', models.TextField(max_length=200)),
            ],
        ),
    ]
