# Generated by Django 4.2.4 on 2023-08-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('six_a_side', '0005_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='gallery_images/'),
        ),
    ]