# Generated by Django 3.2.9 on 2021-11-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
