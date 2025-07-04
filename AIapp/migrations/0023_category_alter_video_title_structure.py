# Generated by Django 4.2.2 on 2023-07-05 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("AIapp", "0022_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="category",
            fields=[
                (
                    "category_name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="video",
            name="Title",
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name="structure",
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
                ("tool_Name", models.CharField(max_length=100)),
                ("tool_Image", models.ImageField(blank=True, upload_to="data")),
                ("tool_Description", models.TextField()),
                ("tool_link", models.URLField(max_length=500)),
                (
                    "category_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="AIapp.category"
                    ),
                ),
            ],
        ),
    ]
