# Generated by Django 4.2.6 on 2023-10-28 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventbuddy', '0004_event_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]