# Generated by Django 4.2.3 on 2023-07-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shipping',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
