# Generated by Django 4.0.2 on 2022-06-10 23:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_neighborhood_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]