# Generated by Django 4.1.2 on 2024-07-10 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='url_nav',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
