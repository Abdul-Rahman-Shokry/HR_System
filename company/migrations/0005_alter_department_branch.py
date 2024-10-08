# Generated by Django 5.1 on 2024-09-03 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_department_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departmentsBranch', to='company.branch'),
        ),
    ]
