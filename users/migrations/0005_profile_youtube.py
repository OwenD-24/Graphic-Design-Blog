# Generated by Django 4.2.16 on 2024-10-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_profile_github_profile_linkedin_profile_twitter"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="youtube",
            field=models.URLField(blank=True, null=True),
        ),
    ]
