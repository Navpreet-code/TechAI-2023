# Generated by Django 4.2.2 on 2023-07-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AIapp", "0021_alter_user_register_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("Title", models.CharField(max_length=100)),
                ("Video", models.FileField(upload_to="")),
            ],
        ),
    ]
