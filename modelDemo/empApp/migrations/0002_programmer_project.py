# Generated by Django 3.1.2 on 2020-11-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('programmer', models.ManyToManyField(to='empApp.Programmer')),
            ],
        ),
    ]
