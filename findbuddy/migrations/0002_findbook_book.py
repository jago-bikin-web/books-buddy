# Generated by Django 4.2.6 on 2023-10-27 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
        ('findbuddy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='findbook',
            name='book',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='book.book'),
        ),
    ]
