# Generated by Django 4.2.6 on 2023-10-28 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
        ('reachbuddy', '0003_alter_thread_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
            preserve_default=False,
        ),
    ]