# Generated by Django 5.0.6 on 2024-10-15 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('studyid', models.AutoField(primary_key=True, serialize=False)),
                ('studyname', models.CharField(max_length=100)),
                ('studyphase', models.CharField(max_length=100)),
                ('studydescription', models.CharField(max_length=100)),
                ('sponsorname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_register.sponsors')),
            ],
        ),
    ]