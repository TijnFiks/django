# Generated by Django 4.1.2 on 2022-10-27 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_department_department_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='department_id',
            new_name='department',
        ),
    ]
