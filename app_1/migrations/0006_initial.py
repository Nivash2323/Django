# Generated by Django 4.2.2 on 2023-07-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_1", "0005_delete_shirts"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shirts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.CharField(max_length=200)),
                ("head", models.CharField(max_length=200)),
                ("discount_price", models.CharField(max_length=10)),
                ("orginal_price", models.CharField(max_length=10)),
                ("discount", models.CharField(max_length=10)),
                ("advertise", models.BooleanField(default="False")),
                ("rating_img", models.ImageField(upload_to="pics")),
                ("day", models.CharField(max_length=10)),
                ("date", models.IntegerField(default=1)),
                ("users", models.CharField(max_length=30)),
                ("type", models.CharField(max_length=20)),
                ("int_discount_price", models.IntegerField()),
                ("int_orginal_price", models.IntegerField()),
                ("fashion_model", models.CharField(max_length=100)),
                ("shop_name", models.CharField(default="None", max_length=100)),
                ("shop_image", models.CharField(default="None", max_length=1000)),
            ],
        ),
    ]
