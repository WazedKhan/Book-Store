# Generated by Django 4.2.1 on 2023-05-24 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_authors_book_authors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors',
            new_name='author',
        ),
    ]