# Generated by Django 4.2.4 on 2023-08-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('six_a_side', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='venue',
            field=models.CharField(max_length=100, null=True),
        ),
    ]