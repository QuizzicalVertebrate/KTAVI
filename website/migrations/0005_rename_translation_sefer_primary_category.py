# Generated by Django 4.1 on 2022-08-15 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0004_sefer_book_sefer_translation"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sefer",
            old_name="translation",
            new_name="primary_category",
        ),
    ]