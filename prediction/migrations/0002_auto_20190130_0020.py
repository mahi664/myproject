# Generated by Django 2.1.5 on 2019-01-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('team1', models.CharField(max_length=200)),
                ('teamlogo1', models.CharField(max_length=200)),
                ('team2', models.CharField(max_length=200)),
                ('teamlogo2', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='matches',
        ),
    ]