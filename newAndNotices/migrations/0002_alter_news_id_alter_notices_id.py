# Generated by Django 5.0.6 on 2024-05-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newAndNotices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notices',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
