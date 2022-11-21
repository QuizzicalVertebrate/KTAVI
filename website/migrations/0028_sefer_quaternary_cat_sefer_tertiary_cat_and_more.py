# Generated by Django 4.1 on 2022-11-20 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0027_remove_sefer_primary_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sefer",
            name="quaternary_cat",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quaternary_cat",
                to="website.quaternarycategory",
            ),
        ),
        migrations.AddField(
            model_name="sefer",
            name="tertiary_cat",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tertiary_cat",
                to="website.tertiarycategory",
            ),
        ),
        migrations.AlterField(
            model_name="sefer",
            name="prime_cat",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prime_cat",
                to="website.primarycategory",
            ),
        ),
        migrations.AlterField(
            model_name="sefer",
            name="secondary_cat",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="secondary_cat",
                to="website.secondarycategory",
            ),
        ),
    ]
