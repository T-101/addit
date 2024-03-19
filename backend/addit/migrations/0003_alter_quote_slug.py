# Generated by Django 5.0.1 on 2024-01-18 15:12

import django_extensions.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addit', '0002_quote_slug_alter_quote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, overwrite=True, populate_from=['topic']),
        ),
    ]