# Generated by Django 4.1.1 on 2022-10-02 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kcaljournal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='calories',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='carbohydrates',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='fat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='fibre',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='protein',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='sugar',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
