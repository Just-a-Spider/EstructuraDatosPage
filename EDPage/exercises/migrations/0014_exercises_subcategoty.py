# Generated by Django 4.2.5 on 2023-11-08 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0013_categories_hassubcategories_types_hassubtypes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercises',
            name='subcategoty',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exercises.subcategories'),
        ),
    ]
