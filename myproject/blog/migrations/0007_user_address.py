# Generated by Django 4.2.6 on 2023-11-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ManyToManyField(to='blog.address'),
        ),
    ]
