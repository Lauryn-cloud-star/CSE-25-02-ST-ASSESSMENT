# Generated by Django 5.2.1 on 2025-05-09 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendorapp", "0002_alter_product_category_alter_product_color_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_id",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("Smart Phones", "Smart Phones"),
                    ("Fashion", "Fashion"),
                    ("Interior Design", "Interior Design"),
                    ("Laptops", "Laptops"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="color",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(
                max_length=100,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9a-zA-Z\\s\\+]+$",
                        "Only alphanumeric characters, spaces and + are allowed.",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
