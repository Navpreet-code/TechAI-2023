# Generated by Django 4.2.2 on 2023-06-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AIapp", "0002_faq_rename_first_name_person_first_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reviews",
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
                ("Title", models.CharField(max_length=10000)),
                ("Message", models.TextField()),
            ],
        ),
    ]
