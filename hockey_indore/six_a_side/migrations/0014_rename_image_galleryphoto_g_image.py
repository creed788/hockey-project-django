# Generated by Django 4.2.4 on 2023-08-22 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('six_a_side', '0013_alter_galleryphoto_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryphoto',
            old_name='image',
            new_name='g_image',
        ),
    ]