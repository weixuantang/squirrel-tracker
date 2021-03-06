# Generated by Django 2.2.7 on 2019-12-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('unique_squirrel_id', models.CharField(max_length=50)),
                ('hectare', models.CharField(max_length=50)),
                ('shift', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('hectare_squirrel_number', models.IntegerField()),
                ('age', models.CharField(max_length=50)),
                ('primary_fur_color', models.CharField(max_length=50)),
                ('highlight_fur_color', models.CharField(max_length=50)),
                ('combination_of_primary_and', models.CharField(max_length=50)),
                ('color_notes', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('above_ground_sighter', models.CharField(max_length=50)),
                ('specific_location', models.CharField(max_length=50)),
                ('running', models.BooleanField()),
                ('chasing', models.BooleanField()),
                ('climbing', models.BooleanField()),
                ('eating', models.BooleanField()),
                ('foraging', models.BooleanField()),
                ('other_activities', models.CharField(max_length=50)),
                ('kuks', models.BooleanField()),
                ('quaas', models.BooleanField()),
                ('moans', models.BooleanField()),
                ('tail_flags', models.BooleanField()),
                ('tail_twitches', models.BooleanField()),
                ('approaches', models.BooleanField()),
                ('indifferent', models.BooleanField()),
                ('runs_from', models.BooleanField()),
                ('other_interactions', models.CharField(max_length=50)),
            ],
        ),
    ]
