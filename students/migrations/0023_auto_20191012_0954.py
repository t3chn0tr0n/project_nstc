# Generated by Django 2.1 on 2019-10-12 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0022_auto_20190430_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='certificate',
            field=models.CharField(default=' ', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='has_certificate',
            field=models.BooleanField(default=False),
        ),
    ]
