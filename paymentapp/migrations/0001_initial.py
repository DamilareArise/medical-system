# Generated by Django 4.2.6 on 2023-11-20 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("serviceapp", "0002_book_service"),
        ("userapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment_service",
            fields=[
                ("payment_id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.BigIntegerField()),
                ("date_of_payment", models.DateTimeField(auto_now_add=True)),
                ("paystack_detail", models.BigIntegerField(unique=True)),
                (
                    "booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="serviceapp.book_service",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userapp.profile",
                    ),
                ),
            ],
        ),
    ]
