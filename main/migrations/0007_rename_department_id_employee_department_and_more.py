# Generated by Django 4.1.2 on 2022-10-27 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_department_employee_department_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='department_id',
            new_name='department',
        ),
        migrations.RemoveField(
            model_name='department',
            name='department_id',
        ),
    ]
