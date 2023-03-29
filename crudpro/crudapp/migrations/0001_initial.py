# Generated by Django 4.1.3 on 2022-12-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.BigIntegerField()),
                ('company', models.CharField(max_length=100)),
                ('salary', models.BigIntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
