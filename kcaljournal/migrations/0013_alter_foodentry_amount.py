# Generated by Django 4.1.5 on 2023-04-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kcaljournal', '0012_alter_foodentry_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodentry',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='grams', max_digits=6),
        ),
    ]
