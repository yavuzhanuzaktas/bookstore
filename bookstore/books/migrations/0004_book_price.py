# Generated by Django 4.2.3 on 2023-07-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_genre_book_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
