# Generated by Django 4.1 on 2022-11-06 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0022_alter_primarycategory_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sefer",
            name="book",
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
