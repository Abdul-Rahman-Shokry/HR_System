# Generated by Django 5.1 on 2024-09-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_branch_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
