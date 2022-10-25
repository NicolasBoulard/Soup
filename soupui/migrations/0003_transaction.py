# Generated by Django 4.1.1 on 2022-10-21 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("soupui", "0002_default_snmp_port"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                ("value", models.CharField(max_length=255)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="soupui.service"
                    ),
                ),
            ],
        ),
    ]