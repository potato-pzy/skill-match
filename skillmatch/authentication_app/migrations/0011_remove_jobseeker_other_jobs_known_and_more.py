# Generated by Django 5.0 on 2025-05-29 07:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication_app", "0010_jobseeker_other_jobs_known"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobseeker",
            name="other_jobs_known",
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_job_provider",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="JobProvider",
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
                ("company_name", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.TextField()),
                (
                    "profile",
                    models.ImageField(
                        blank=True, null=True, upload_to="provider_profiles/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_provider_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
