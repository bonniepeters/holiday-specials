# Generated by Django 2.2.7 on 2019-11-07 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday_specials', '0003_auto_20191106_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='episode',
            name='season',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='show',
            name='genre',
            field=models.CharField(choices=[('comedy', 'Comedy'), ('drama', 'Drama')], default='comedy', max_length=6),
        ),
        migrations.AlterField(
            model_name='show',
            name='streaming_on',
            field=models.CharField(choices=[('hulu', 'Hulu'), ('other', 'Other'), ('netflix', 'Netflix'), ('amazon prime', 'Amazon Prime'), ('hbo', 'HBO')], default='netflix', max_length=20),
        ),
    ]