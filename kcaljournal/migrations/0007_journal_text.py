# Generated by Django 4.1.2 on 2023-01-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kcaljournal', '0006_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='text',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
