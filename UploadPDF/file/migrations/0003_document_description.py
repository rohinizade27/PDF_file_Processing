# Generated by Django 3.1.5 on 2021-01-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_remove_document_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
