# Generated by Django 5.0.2 on 2024-04-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KitchenOwner', '0004_kitchen_is_negotiable'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='city',
            field=models.CharField(choices=[('Riyadh', 'الرياض'), ('Jeddah', 'جدة'), ('Dammam', 'الدمام')], default='Riyadh', max_length=100),
            preserve_default=False,
        ),
    ]
