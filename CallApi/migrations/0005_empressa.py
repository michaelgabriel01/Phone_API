# Generated by Django 2.0.6 on 2018-06-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CallApi', '0004_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empressa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('company_location', models.CharField(max_length=20)),
                ('number_of_employees', models.IntegerField()),
                ('employees_avarage_salary', models.BigIntegerField()),
                ('created_day_and_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]