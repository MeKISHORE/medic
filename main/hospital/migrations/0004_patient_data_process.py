# Generated by Django 2.2 on 2019-08-28 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20190828_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_data',
            name='process',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]