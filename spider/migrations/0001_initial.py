# Generated by Django 2.0 on 2018-12-22 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageItem',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]