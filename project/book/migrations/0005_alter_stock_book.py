# Generated by Django 4.2.1 on 2023-05-24 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]
