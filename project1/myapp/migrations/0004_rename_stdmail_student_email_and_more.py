# Generated by Django 5.0.3 on 2024-04-04 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stdmail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stdname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stdpass',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='stdid',
        ),
    ]
