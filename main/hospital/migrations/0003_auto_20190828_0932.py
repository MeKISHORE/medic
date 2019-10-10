# Generated by Django 2.2 on 2019-08-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=30)),
                ('hospital_id', models.CharField(max_length=30)),
                ('P_name', models.CharField(max_length=20)),
                ('A_name', models.CharField(max_length=150)),
                ('Mobile', models.IntegerField(max_length=15)),
                ('P_address', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='patient',
        ),
    ]