# Generated by Django 2.1.1 on 2018-09-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20180903_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admision_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='registration_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
