# Generated by Django 5.0.3 on 2024-03-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdid', models.IntegerField()),
                ('stdname', models.CharField(max_length=70)),
                ('stdmail', models.EmailField(max_length=70)),
                ('stdpass', models.CharField(max_length=70)),
            ],
        ),
    ]
