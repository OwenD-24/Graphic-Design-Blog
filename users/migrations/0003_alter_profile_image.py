# Generated by Django 4.2.16 on 2024-10-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_lahajp.webp', upload_to='profile_pics'),
        ),
    ]
