# Generated by Django 4.2.6 on 2023-10-28 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
        ('eventbuddy', '0006_event_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='book',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]
