# Generated by Django 5.0.6 on 2024-07-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_book_image_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="pdf_url",
            field=models.TextField(blank=True, null=True),
        ),
    ]
