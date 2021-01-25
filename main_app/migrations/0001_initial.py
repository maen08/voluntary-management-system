# Generated by Django 3.1.5 on 2021-01-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemActivitie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirement', models.TextField()),
                ('place', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now=True)),
                ('duration', models.IntegerField()),
                ('people_required', models.IntegerField()),
                ('organization', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('skill', models.CharField(max_length=50)),
            ],
        ),
    ]
